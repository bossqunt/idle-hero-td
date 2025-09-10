from flask import Blueprint, jsonify, request, Response, render_template
import sqlite3
import os
import json
from collections import OrderedDict
from models import db, Hero, SynergyDetail, basedir
api = Blueprint('api', __name__)


@api.route('/api/synergies')
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

@api.route('/api/heroes')
def api_heroes():
    heroes = Hero.query.all()
    return jsonify([{'hero_id': h.hero_id, 'name': h.name} for h in heroes])

@api.route('/api/attributes')
def api_attributes():
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT attribute FROM synergy_details')
    attributes = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(attributes)

@api.route('/api/bonus_types')
def api_bonus_types():
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT bonus_type FROM synergy_details')
    bonus_types = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(bonus_types)

@api.route('/api/tiers')
def api_tiers():
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT tier FROM synergy_details')
    tiers = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(tiers)

@api.route('/api/ranks')
def api_ranks():
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT rank_required FROM synergy_details')
    ranks = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(ranks)

@api.route('/api/levelup-attributes')
def api_levelup_attributes():
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT attribute FROM hero_level_bonus')
    attributes = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(attributes)


@api.route('/api/heroes/levelup')
def api_heroes_levelup():
    hero_list = []
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    heroes = Hero.query.all()
    for hero in heroes:
        cursor.execute('SELECT level, bonus, bonus_type, attribute, global, personal FROM hero_level_bonus WHERE hero_id=?', (hero.hero_id,))
        bonuses = []
        for row in cursor.fetchall():
            bonuses.append(OrderedDict([
                ('level', row[0]),
                ('attribute', row[3]),
                ('value', row[1]),
                ('type', row[2]),
                ('scope', {
                    'global': bool(row[4]),
                    'personal': bool(row[5])
                })
            ]))
        hero_dict = OrderedDict()
        hero_dict['id'] = hero.hero_id
        hero_dict['name'] = hero.name
        hero_dict['bonuses'] = bonuses
        hero_list.append(hero_dict)
    conn.close()
    result = OrderedDict()
    result['heroes'] = hero_list
    return Response(json.dumps(result, ensure_ascii=False, sort_keys=False), mimetype='application/json')

@api.route('/api/synergy', methods=['POST'])
def api_synergy_save():
    data = request.json
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
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

@api.route('/api/synergy/<int:synergy_id>', methods=['DELETE'])
def api_synergy_delete(synergy_id):
    conn = sqlite3.connect(os.path.join(basedir, 'idleherotd.db'))
    cursor = conn.cursor()
    cursor.execute('DELETE FROM synergy_details WHERE id=?', (synergy_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})
