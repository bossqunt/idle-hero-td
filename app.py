from flask import Flask, jsonify, request
from flask import render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField, SelectMultipleField
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.secret_key = "idleherotd-super-secret-key-2025"
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'idleherotd.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
admin = Admin(app, name='Idle Hero TD Admin', template_mode='bootstrap3')

# SQLAlchemy models
class Hero(db.Model):
    __tablename__ = 'heroes'
    hero_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    skill = db.Column(db.String)
    ability = db.Column(db.String)
    cd = db.Column(db.Integer)
    description = db.Column(db.String)
    value = db.Column(db.Integer)
    time = db.Column(db.Integer)

class SynergyDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer)
    synergy_ids = db.Column(db.String)
    attribute = db.Column(db.String)
    bonus_type = db.Column(db.String)
    bonus = db.Column(db.Integer)
    global_ = db.Column(db.Boolean)
    personal = db.Column(db.Boolean)
    tier = db.Column(db.Integer)
    rank_required = db.Column(db.Integer)


# Custom SynergyDetail admin view
class SynergyDetailAdmin(ModelView):
    form_overrides = {
        'hero_id': SelectField,
        'synergy_ids': SelectMultipleField,
        'attribute': SelectField,
        'bonus_type': SelectField,
        'tier': SelectField,
        'rank_required': SelectField,
    }

    def _get_choices(self):
        # Get all choices from DB
        hero_choices = [(str(h.hero_id), h.name) for h in Hero.query.all()]
        attribute_choices = [(a.attribute, a.attribute.replace('_', ' ')) for a in db.session.query(SynergyDetail.attribute).distinct()]
        bonus_type_choices = [(b.bonus_type, b.bonus_type) for b in db.session.query(SynergyDetail.bonus_type).distinct()]
        tier_choices = [(str(t.tier), f'Tier {t.tier}') for t in db.session.query(SynergyDetail.tier).distinct()]
        rank_choices = [(str(r.rank_required), str(r.rank_required)) for r in db.session.query(SynergyDetail.rank_required).distinct()]
        return hero_choices, attribute_choices, bonus_type_choices, tier_choices, rank_choices

    def create_form(self, obj=None):
        form = super().create_form(obj)
        hero_choices, attribute_choices, bonus_type_choices, tier_choices, rank_choices = self._get_choices()
        form.hero_id.choices = hero_choices
        form.synergy_ids.choices = hero_choices
        form.attribute.choices = attribute_choices
        form.bonus_type.choices = bonus_type_choices
        form.tier.choices = tier_choices
        form.rank_required.choices = rank_choices
        return form

    def edit_form(self, obj=None):
        form = super().edit_form(obj)
        hero_choices, attribute_choices, bonus_type_choices, tier_choices, rank_choices = self._get_choices()
        form.hero_id.choices = hero_choices
        form.synergy_ids.choices = hero_choices
        form.attribute.choices = attribute_choices
        form.bonus_type.choices = bonus_type_choices
        form.tier.choices = tier_choices
        form.rank_required.choices = rank_choices
        return form

    column_list = ('hero_id', 'synergy_ids', 'attribute', 'bonus_type', 'bonus', 'global_', 'personal', 'tier', 'rank_required')
    column_labels = {
        'hero_id': 'Hero',
        'synergy_ids': 'Synergy Heroes',
        'attribute': 'Attribute',
        'bonus_type': 'Bonus Type',
        'bonus': 'Bonus',
        'global_': 'Global',
        'personal': 'Personal',
        'tier': 'Tier',
        'rank_required': 'Rank Required'
    }
    def _display_hero_name(self, context, model, name):
        hero = Hero.query.get(model.hero_id)
        return hero.name if hero else model.hero_id
    column_formatters = {
        'hero_id': _display_hero_name
    }
# Synergies Editor page
@app.route('/synergies-editor')
def synergies_editor_page():
    return render_template('synergies_editor.html', active_nav='synergies')

# API endpoints for editor
@app.route('/api/synergies')
def api_synergies():
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT hero_id, synergy_ids, attribute, bonus_type, bonus, `global`, `personal`, tier, rank_required FROM synergy_details')
    rows = []
    for row in cursor.fetchall():
        ids = []
        synergy_name = None
        for sid in row[2].split(','):
            sid = sid.strip()
            if not sid:
                continue
            try:
                ids.append(int(sid))
            except ValueError:
                synergy_name = sid
        rows.append({
            'id': row[0],
            'hero_id': row[1],
            'synergy_ids': ids,
            'synergy_name': synergy_name,
            'attribute': row[3],
            'bonus_type': row[4],
            'bonus': row[5],
            'global': bool(row[6]),
            'personal': bool(row[7]),
            'tier': row[8],
            'rank_required': row[9] if len(row) > 9 else None
        })
    conn.close()
    return jsonify(rows)

@app.route('/api/heroes')
def api_heroes():
    heroes = Hero.query.all()
    return jsonify([{'hero_id': h.hero_id, 'name': h.name} for h in heroes])

@app.route('/api/attributes')
def api_attributes():
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT attribute FROM synergy_details')
    attributes = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(attributes)

@app.route('/api/bonus_types')
def api_bonus_types():
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT bonus_type FROM synergy_details')
    bonus_types = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(bonus_types)

@app.route('/api/tiers')
def api_tiers():
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT tier FROM synergy_details')
    tiers = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(tiers)

@app.route('/api/ranks')
def api_ranks():
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT rank_required FROM synergy_details')
    ranks = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(ranks)

@app.route('/api/levelup-attributes')
def api_levelup_attributes():
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT attribute FROM hero_level_bonus')
    attributes = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(attributes)

admin.add_view(SynergyDetailAdmin(SynergyDetail, db.session))


@app.route('/hero/<int:hero_id>')
def get_hero(hero_id):
    h = Hero.query.get(hero_id)
    if not h:
        return jsonify({'error': 'Hero not found'}), 404
    return jsonify({
        'hero_id': h.hero_id,
        'name': h.name,
        'skill': h.skill,
        'ability': h.ability,
        'cd': h.cd,
        'description': h.description,
        'value': h.value,
        'time': h.time
    })


# /heroes and / show only hero data
@app.route('/')

def index_page():
    heroes = Hero.query.all()
    return render_template('heroes.html', heroes=heroes, active_nav='heroes')

@app.route('/heroes')

def heroes_page():
    heroes = Hero.query.all()
    return render_template('heroes.html', heroes=heroes, active_nav='heroes')
 


# /levelup shows milestone table
@app.route('/levelup')

def levelup_page():
    heroes = Hero.query.all()
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT level FROM hero_level_bonus ORDER BY level')
    levels = [row[0] for row in cursor.fetchall()]
    cursor.execute('SELECT DISTINCT attribute FROM hero_level_bonus')
    attributes = [row[0] for row in cursor.fetchall()]
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
@app.route('/api/heroes')
def api_get_heroes():
    heroes = Hero.query.all()
    return jsonify([
        {
            'hero_id': h.hero_id,
            'name': h.name,
            'skill': h.skill,
            'ability': h.ability,
            'cd': h.cd,
            'description': h.description,
            'value': h.value,
            'time': h.time
        } for h in heroes
    ])

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


@app.route('/api/synergy', methods=['POST'])
def api_synergy_save():
    data = request.json
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    # If id is present, update; else, insert new
    if data.get('id'):
        cursor.execute('''
            UPDATE synergy_details SET hero_id=?, synergy_ids=?, attribute=?, bonus_type=?, bonus=?, global=?, personal=?, tier=?, rank_required=? WHERE id=?
        ''', (
            data['hero_id'],
            ','.join(str(sid) for sid in data['synergy_ids']),
            data['attribute'],
            data['bonus_type'],
            data['bonus'],
            int(data['global']),
            int(data['personal']),
            data['tier'],
            data['rank_required'],
            data['id']
        ))
    else:
        cursor.execute('''
            INSERT INTO synergy_details (hero_id, synergy_ids, attribute, bonus_type, bonus, global, personal, tier, rank_required)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['hero_id'],
            ','.join(str(sid) for sid in data['synergy_ids']),
            data['attribute'],
            data['bonus_type'],
            data['bonus'],
            int(data['global']),
            int(data['personal']),
            data['tier'],
            data['rank_required']
        ))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/synergy/<int:synergy_id>', methods=['DELETE'])
def api_synergy_delete(synergy_id):
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('DELETE FROM synergy_details WHERE id=?', (synergy_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
