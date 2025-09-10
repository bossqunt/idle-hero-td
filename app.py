from flask import Flask, jsonify, request, Response
import json
from api import api
from flask import render_template
import os
import sqlite3
from models import db, Hero, SynergyDetail, basedir
from flask import send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.register_blueprint(api)
app.secret_key = "idleherotd-super-secret-key-2025"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'idleherotd.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
SWAGGER_URL = '/swagger'
API_URL = '/openapi.json'  # Path to your OpenAPI spec

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Idle Hero TD API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/openapi.json')
def openapi_json():
    return send_from_directory('.', 'openapi.json')

# Synergies Editor page
@app.route('/synergies-editor')
def synergies_editor_page():
    return render_template('synergies_editor.html', active_nav='synergies')


# /heroes and / show only hero data
@app.route('/')
def index_page():
    heroes = Hero.query.all()
    return render_template('heroes.html', heroes=heroes, active_nav='heroes')

@app.route('/heroes')
def heroes_page():
    heroes = Hero.query.all()
    return render_template('heroes.html', heroes=heroes, active_nav='heroes')
 
# Page render endpoint (in app.py)
@app.route('/levelup')
def levelup_page():
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT level FROM hero_level_bonus ORDER BY level')
    levels = [row[0] for row in cursor.fetchall()]
    cursor.execute('SELECT DISTINCT attribute FROM hero_level_bonus')
    attributes = [row[0] for row in cursor.fetchall()]
    heroes = Hero.query.all()
    hero_rows = []
    for hero in heroes:
        cursor.execute('SELECT level, bonus, bonus_type, attribute, global, personal FROM hero_level_bonus WHERE hero_id=?', (hero.hero_id,))
        bonuses = {row[0]: {
            'bonus': row[1],
            'bonus_type': row[2],
            'attribute': row[3],
            'global': row[4],
            'personal': row[5]
        } for row in cursor.fetchall()}
        hero_rows.append({
            'name': hero.name,
            'bonuses': bonuses
        })
    conn.close()
    return render_template('levelup.html', levels=levels, hero_rows=hero_rows, attributes=attributes, active_nav='levelup')
    # API route for hero data


# /synergies page: hero synergies table
@app.route('/synergies')
def synergies_page():
    heroes = Hero.query.all()
    hero_names = {h.hero_id: h.name for h in heroes}
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT hero_id, synergy_ids, attribute, bonus_type, bonus, global, personal, tier, rank_required FROM synergy_details ORDER BY hero_id, tier')
    synergy_rows = []
    seen = set()
    for row in cursor.fetchall():
        hero_id = row[0]
        ids = []
        synergy_name = None
        for sid in row[1].split(','):
            sid = sid.strip()
            if not sid:
                continue
            try:
                ids.append(int(sid))
            except ValueError:
                synergy_name = sid
        # Remove duplicates by hero_id, tier, synergy_ids, synergy_name
        key = (hero_id, row[7], tuple(ids), synergy_name)
        if key in seen:
            continue
        seen.add(key)
        synergy_rows.append({
            'hero_name': hero_names.get(hero_id, hero_id),
            'tier': row[7],
            'synergy_ids': ids,
            'synergy_name': synergy_name,
            'attribute': row[2],
            'bonus_type': row[3],
            'bonus': row[4],
            'global': row[5],
            'personal': row[6],
            'rank_required': row[8]
        })
    conn.close()
    return render_template('synergies.html', synergy_rows=synergy_rows, hero_names=hero_names, active_nav='synergies')




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
