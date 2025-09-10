import sqlite3
from data import hero_list, synergies, hero_data

conn = sqlite3.connect('idleherotd.db')
c = conn.cursor()

# Create tables
c.execute('''
CREATE TABLE IF NOT EXISTS heroes (
    hero_id INTEGER PRIMARY KEY,
    name TEXT,
    skill TEXT,
    ability TEXT,
    cd INTEGER,
    description TEXT,
    value INTEGER,
    time INTEGER
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS synergy_details (
    hero_id INTEGER,
    synergy_ids TEXT,
    attribute TEXT,
    bonus_type TEXT,
    bonus INTEGER,
    global BOOLEAN,
    personal BOOLEAN,
    tier INTEGER,
    rank_required INTEGER,
    FOREIGN KEY(hero_id) REFERENCES heroes(hero_id)
)
''')


c.execute('''
CREATE TABLE IF NOT EXISTS synergies (
    hero_id INTEGER PRIMARY KEY,
    FOREIGN KEY(hero_id) REFERENCES heroes(hero_id)
)
''')

# New table for hero_data
c.execute('''
CREATE TABLE IF NOT EXISTS hero_level_bonus (
    hero_id INTEGER,
    level INTEGER,
    bonus INTEGER,
    bonus_type TEXT,
    attribute TEXT,
    global BOOLEAN,
    personal BOOLEAN,
    FOREIGN KEY(hero_id) REFERENCES heroes(hero_id)
)
''')

# Insert heroes
def insert_heroes():
    for hero in hero_list:
        c.execute('''
            INSERT OR IGNORE INTO heroes (hero_id, name, skill, ability, cd, description, value, time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            hero.get('id'),
            hero.get('name'),
            hero.get('skill'),
            hero.get('ability'),
            hero.get('cd'),
            hero.get('description'),
            hero.get('value'),
            hero.get('time')
        ))


# Insert synergies
def insert_synergies():
    for entry in synergies:
        hero_id = entry['hero_id']
        c.execute('''
            INSERT OR REPLACE INTO synergies (hero_id) VALUES (?)
        ''', (hero_id,))
        for detail in entry['synergies']:
            c.execute('''
                INSERT OR IGNORE INTO  synergy_details (hero_id, synergy_ids, attribute, bonus_type, bonus, global, personal, tier, rank_required)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                hero_id,
                ','.join(str(sid) for sid in detail['synergy_ids']),
                detail['attribute'],
                detail['bonus_type'],
                detail['bonus'],
                int(detail['global']),
                int(detail['personal']),
                detail['tier'],
                detail['rank_required']
            ))



# Insert hero_data
def insert_hero_level_bonus():
    for hero_id_str, bonuses in hero_data.items():
        hero_id = int(hero_id_str)
        for bonus in bonuses:
            c.execute('''
                INSERT OR IGNORE INTO hero_level_bonus (hero_id, level, bonus, bonus_type, attribute, global, personal)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                hero_id,
                bonus['level'],
                bonus['bonus'],
                bonus['bonus_type'],
                bonus['attribute'],
                int(bonus['global']),
                int(bonus['personal'])
            ))


insert_heroes()
insert_synergies()
insert_hero_level_bonus()
conn.commit()
conn.close()
print('Database setup complete.')
