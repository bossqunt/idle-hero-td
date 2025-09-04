
from flask import Flask, jsonify, send_file
from flask import render_template_string, send_from_directory
from streamlit import html
app = Flask(__name__)

# Endpoint to retrieve all heroes data
@app.route("/heroes", methods=["GET"])
def get_heroes():
    return jsonify(hero_list)

# Endpoint to retrieve all level-up milestone data
@app.route("/levelup", methods=["GET"])
def get_levelup():
    return jsonify(monster_data)

# New endpoint to return merged table data

# Swagger UI endpoint
@app.route("/docs")
def swagger_ui():
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>IdleHeroTD API Docs</title>
                <link rel=\"stylesheet\" href=\"https://unpkg.com/swagger-ui-dist/swagger-ui.css\" />
        </head>
        <body>
            <div id="swagger-ui"></div>
            <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
            <script>
                window.onload = function() {
                    SwaggerUIBundle({
                        url: '/openapi.json',
                        dom_id: '#swagger-ui'
                    });
                }
            </script>
        </body>
        </html>
        """
            return render_template_string(html)

# Serve OpenAPI spec
@app.route("/openapi.json")
def openapi_spec():
        return send_from_directory(".", "openapi.json")


@app.route("/table", methods=["GET"])
def table():
    hero_names = {str(hero["id"]): hero["name"] for hero in hero_list}
    table = []
    for monster_id, bonuses in monster_data.items():
        row = {"hero": hero_names.get(monster_id, monster_id)}
        for lvl in levels:
            cell = None
            for entry in bonuses:
                if entry["level"] == lvl:
                    sign = "+" if entry["bonus"] >= 0 else ""
                    bonus_str = f"{sign}{entry['bonus']} {entry['attribute'].replace('_', ' ').title()}"
                    if entry["bonus_type"] == "percent":
                        bonus_str += "%"
                    cell = {
                        "bonus": bonus_str,
                        "global": entry.get("global", False),
                        "personal": entry.get("personal", False)
                    }
                    break
            row[f"level {lvl}"] = cell if cell else {"bonus": "", "global": False, "personal": False}
        table.append(row)
    columns = ["hero"] + [f"level {lvl}" for lvl in levels]
    return jsonify({"table": table, "columns": columns})

hero_list = [
    {"id": 1, "name": "Militia", "skill": "Spin Attack", "ability": "damage", "cd": 24, "description": "Instantly deal 300% damage to all enemies within range", "value": 300, "time": 1},
    {"id": 2, "name": "Apprentice", "skill": "Shield Slam", "cd": 10, "description": "Stuns an enemy and reduces incoming damage for 3s.", "value": 80, "time": 3},
    {"id": 3, "name": "Scout", "skill": "Nature’s Grasp", "cd": 12, "description": "Roots enemies in place while healing nearby allies.", "value": 60, "time": 4},
    {"id": 4, "name": "Viking", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 5, "name": "Druid", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 6, "name": "Hunter", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 7, "name": "Ninja", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 8, "name": "Sorcerer", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 9, "name": "Forester", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},               
    {"id": 10, "name": "Assassin", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 11, "name": "Witch", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 12, "name": "Archer", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 13, "name": "Peacekeeper", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 14, "name": "Wizard", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 15, "name": "Ranger", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 16, "name": "Samurai", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 17, "name": "Elementalist", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 18, "name": "Arbalest", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 19, "name": "Paladin", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 20, "name": "Battlemage", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 21, "name": "Sniper", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 22, "name": "Gladiator", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 23, "name": "Spelldancer", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 24, "name": "Rogue", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 25, "name": "Berserker", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 26, "name": "Skymage", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 27, "name": "Ballista", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 28, "name": "Chieftain", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 29, "name": "Warlock", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 30, "name": "Crusader", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 31, "name": "Champion", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 32, "name": "Templar", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 33, "name": "Captain", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 34, "name": "Warlord", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 35, "name": "Necromancer", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
    {"id": 36, "name": "Warden", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
]

synergy_data = {
    "tier": 2,
    "hero": [101, 104, 109, 113],
    "rank": 1,
    "global": True,
    "personal": False
}

levels = [25, 75, 150, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 6000, 7500]

monster_data = {
        "1": [
        {"level": 25, "bonus": 10, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
        {"level": 75, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
        {"level": 150, "bonus": 30, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
        {"level": 250, "bonus": 10, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
        {"level": 500, "bonus": 5, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
        {"level": 750, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
        {"level": 1000, "bonus": -16, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
        {"level": 1500, "bonus": 16, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
        {"level": 2000, "bonus": 4, "bonus_type": "percent", "attribute": "super_crit_chance", "global": True, "personal": False},
        {"level": 2500, "bonus": 30, "bonus_type": "percent", "attribute": "super_gold_amount", "global": True, "personal": False},
        {"level": 3000, "bonus": 36, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
        {"level": 3500, "bonus": 15, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
        {"level": 4000, "bonus": 5, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
        {"level": 5000, "bonus": 2, "bonus_type": "percent", "attribute": "ultra_energy_chance", "global": True, "personal": False},
        {"level": 6000, "bonus": 25, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
        {"level": 7500, "bonus": 30, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": False, "personal": True}
    ],
        "2": [
            {"level": 25, "bonus": 5, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
            {"level": 75, "bonus": -2, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
            {"level": 150, "bonus": 8, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
            {"level": 250, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 500, "bonus": 3, "bonus_type": "fixed", "attribute": "skill_duration", "global": True, "personal": False},
            {"level": 750, "bonus": 18, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 1000, "bonus": 21, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
            {"level": 1500, "bonus": 17, "bonus_type": "percent", "attribute": "range", "global": True, "personal": False},
            {"level": 2000, "bonus": 90, "bonus_type": "percent", "attribute": "super_gold_amount", "global": False, "personal": True},
            {"level": 2500, "bonus": 10, "bonus_type": "percent", "attribute": "super_exp_amount", "global": True, "personal": False},
            {"level": 3000, "bonus": 1, "bonus_type": "percent", "attribute": "ultra_crit_chance", "global": True, "personal": False},
            {"level": 3500, "bonus": 2, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
            {"level": 4000, "bonus": 175, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
            {"level": 5000, "bonus": 75, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
            {"level": 6000, "bonus": 5, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
            {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "super_crit_damage", "global": True, "personal": False}
        ],
        "3": [
            {"level": 25, "bonus": 3, "bonus_type": "percent", "attribute": "kill_gold", "global": True, "personal": False},
            {"level": 75, "bonus": 10, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
            {"level": 150, "bonus": 9, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 250, "bonus": -10, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
            {"level": 500, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 750, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 1000, "bonus": 5, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
            {"level": 1500, "bonus": 80, "bonus_type": "percent", "attribute": "super_crit_damage", "global": False, "personal": True},
            {"level": 2000, "bonus": 1, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
            {"level": 2500, "bonus": 6, "bonus_type": "percent", "attribute": "super_exp_chance", "global": True, "personal": False},
            {"level": 3000, "bonus": 125, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
            {"level": 3500, "bonus": 2, "bonus_type": "percent", "attribute": "ultra_gold_chance", "global": True, "personal": False},
            {"level": 4000, "bonus": 20, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
            {"level": 5000, "bonus": 65, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
            {"level": 6000, "bonus": 100, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False}
        ],
        "4": [
            {"level": 25, "bonus": 5, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
            {"level": 75, "bonus": 6, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
            {"level": 150, "bonus": 9, "bonus_type": "percent", "attribute": "kill_gold", "global": True, "personal": False},
            {"level": 250, "bonus": 12, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 500, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 750, "bonus": 13, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
            {"level": 1000, "bonus": 5, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
            {"level": 1500, "bonus": 2, "bonus_type": "percent", "attribute": "super_exp_chance", "global": True, "personal": False},
            {"level": 2000, "bonus": -20, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
            {"level": 2500, "bonus": 20, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
            {"level": 3000, "bonus": 125, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
            {"level": 3500, "bonus": 2, "bonus_type": "percent", "attribute": "ultra_crit_chance", "global": True, "personal": False},
            {"level": 4000, "bonus": 175, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": False, "personal": True},
            {"level": 5000, "bonus": 20, "bonus_type": "percent", "attribute": "super_crit_chance", "global": True, "personal": False},
            {"level": 6000, "bonus": 5, "bonus_type": "fixed", "attribute": "skill_power", "global": True, "personal": False},
            {"level": 7500, "bonus": 5, "bonus_type": "percent", "attribute": "boss_exp", "global": True, "personal": False}
        ],
        "5": [
            {"level": 25, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
            {"level": 75, "bonus": 20, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
            {"level": 150, "bonus": 9, "bonus_type": "percent", "attribute": "kill_gold", "global": True, "personal": False},
            {"level": 250, "bonus": 40, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
            {"level": 500, "bonus": 12, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
            {"level": 750, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 1000, "bonus": 8, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
            {"level": 1500, "bonus": -8, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
            {"level": 2000, "bonus": 4, "bonus_type": "percent", "attribute": "super_crit_chance", "global": True, "personal": False},
            {"level": 2500, "bonus": 20, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
            {"level": 3000, "bonus": 4, "bonus_type": "percent", "attribute": "ultra_gold_chance", "global": False, "personal": True},
            {"level": 3500, "bonus": 4, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
            {"level": 4000, "bonus": 50, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 5000, "bonus": 25, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
            {"level": 6000, "bonus": 100, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
            {"level": 7500, "bonus": 25, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True}
        ],
        "6": [
            {"level": 25, "bonus": 5, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
            {"level": 75, "bonus": 6, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
            {"level": 150, "bonus": 6, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
            {"level": 250, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 500, "bonus": 12, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
            {"level": 750, "bonus": 6, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
            {"level": 1000, "bonus": 70, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
            {"level": 1500, "bonus": 2, "bonus_type": "percent", "attribute": "super_gold_chance", "global": True, "personal": False},
            {"level": 2000, "bonus": -9, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
            {"level": 2500, "bonus": 5, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 3000, "bonus": 10, "bonus_type": "percent", "attribute": "ultra_crit_chance", "global": True, "personal": False},
            {"level": 3500, "bonus": 42, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 4000, "bonus": 3, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
            {"level": 5000, "bonus": 15, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 6000, "bonus": 250, "bonus_type": "percent", "attribute": "super_gold_amount", "global": False, "personal": True},
            {"level": 7500, "bonus": 10, "bonus_type": "percent", "attribute": "instant_skill_chance", "global": False, "personal": True}
        ],
        "7": [
                        {"level": 25, "bonus": 5, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                        {"level": 75, "bonus": 1, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
                        {"level": 150, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                        {"level": 250, "bonus": 20, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
                        {"level": 500, "bonus": -5, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
                        {"level": 750, "bonus": 6, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                        {"level": 1000, "bonus": 3, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                        {"level": 1500, "bonus": 80, "bonus_type": "percent", "attribute": "super_crit_damage", "global": True, "personal": False},
                        {"level": 2000, "bonus": 12, "bonus_type": "percent", "attribute": "super_gold_chance", "global": False, "personal": True},
                        {"level": 2500, "bonus": 30, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                        {"level": 3000, "bonus": 3, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                        {"level": 3500, "bonus": 2, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
                        {"level": 4000, "bonus": 50, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
                        {"level": 5000, "bonus": 6, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                        {"level": 6000, "bonus": 100, "bonus_type": "percent", "attribute": "super_gold_amount", "global": True, "personal": False},
                        {"level": 7500, "bonus": 20, "bonus_type": "percent", "attribute": "super_energy_amount", "global": True, "personal": False}
                    ], 
"8": [
    {"level": 25, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
    {"level": 75, "bonus": 6, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
    {"level": 150, "bonus": 9, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
    {"level": 250, "bonus": 4, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
    {"level": 500, "bonus": 15, "bonus_type": "percent", "attribute": "kill_gold", "global": True, "personal": False},
    {"level": 750, "bonus": 30, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
    {"level": 1000, "bonus": -16, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
    {"level": 1500, "bonus": 8, "bonus_type": "percent", "attribute": "super_crit_chance", "global": True, "personal": False},
    {"level": 2000, "bonus": 18, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
    {"level": 2500, "bonus": 8, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
    {"level": 3000, "bonus": 125, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
    {"level": 3500, "bonus": 15, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
    {"level": 4000, "bonus": 175, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": False, "personal": True},
    {"level": 5000, "bonus": 75, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": False, "personal": True},
    {"level": 6000, "bonus": 25, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
    {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": True, "personal": False}
],
        "9": [
            {"level": 25, "bonus": 10, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
            {"level": 75, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 150, "bonus": 30, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
            {"level": 250, "bonus": 12, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 500, "bonus": 3, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
            {"level": 750, "bonus": 30, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
            {"level": 1000, "bonus": 15, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
            {"level": 1500, "bonus": 2, "bonus_type": "percent", "attribute": "super_exp_chance", "global": True, "personal": False},
            {"level": 2000, "bonus": 7, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
            {"level": 2500, "bonus": -22, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
            {"level": 3000, "bonus": 125, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
            {"level": 3500, "bonus": 42, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": True, "personal": False},
            {"level": 4000, "bonus": 5, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
            {"level": 5000, "bonus": 4, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
            {"level": 6000, "bonus": 10, "bonus_type": "percent", "attribute": "super_crit_chance", "global": True, "personal": False},
            {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "super_crit_damage", "global": True, "personal": False}
        ],
"10": [
    {"level": 25, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
    {"level": 75, "bonus": 6, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
    {"level": 150, "bonus": 8, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
    {"level": 250, "bonus": -4, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
    {"level": 500, "bonus": 25, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
    {"level": 750, "bonus": 13, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
    {"level": 1000, "bonus": 21, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
    {"level": 1500, "bonus": 24, "bonus_type": "percent", "attribute": "super_gold_amount", "global": False, "personal": True},
    {"level": 2000, "bonus": 4, "bonus_type": "percent", "attribute": "super_exp_chance", "global": True, "personal": False},
    {"level": 2500, "bonus": 8, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
    {"level": 3000, "bonus": 4, "bonus_type": "percent", "attribute": "ultra_crit_chance", "global": True, "personal": False},
    {"level": 3500, "bonus": 42, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
    {"level": 4000, "bonus": 20, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
    {"level": 5000, "bonus": -25, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
    {"level": 6000, "bonus": 250, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
    {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": False, "personal": True}
],
"11": [
    {"level": 25, "bonus": 2, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
    {"level": 75, "bonus": 1, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
    {"level": 150, "bonus": 8, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
    {"level": 250, "bonus": 40, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
    {"level": 500, "bonus": -12, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
    {"level": 750, "bonus": 60, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
    {"level": 1000, "bonus": 70, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
    {"level": 1500, "bonus": 6, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
    {"level": 2000, "bonus": 4, "bonus_type": "percent", "attribute": "super_exp_chance", "global": True, "personal": False},
    {"level": 2500, "bonus": 5, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
    {"level": 3000, "bonus": 1, "bonus_type": "percent", "attribute": "ultra_gold_chance", "global": True, "personal": False},
    {"level": 3500, "bonus": 42, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
    {"level": 4000, "bonus": 8, "bonus_type": "percent", "attribute": "ultra_crit_chance", "global": False, "personal": True},
    {"level": 5000, "bonus": 4, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
    {"level": 6000, "bonus": 100, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
    {"level": 7500, "bonus": 12, "bonus_type": "percent", "attribute": "super_crit_chance", "global": True, "personal": False}
],
        "12": [
            {"level": 25, "bonus": 10, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 75, "bonus": 2, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
            {"level": 150, "bonus": 8, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
            {"level": 250, "bonus": 40, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
            {"level": 500, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_power", "global": True, "personal": False},
            {"level": 750, "bonus": 18, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
            {"level": 1000, "bonus": 3, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 1500, "bonus": -8, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
            {"level": 2000, "bonus": 12, "bonus_type": "percent", "attribute": "super_crit_chance", "global": False, "personal": True},
            {"level": 2500, "bonus": 20, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
            {"level": 3000, "bonus": 36, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 3500, "bonus": 4, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
            {"level": 4000, "bonus": 175, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": False, "personal": True},
            {"level": 5000, "bonus": 15, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 6000, "bonus": 15, "bonus_type": "percent", "attribute": "super_exp_amount", "global": True, "personal": False},
            {"level": 7500, "bonus": 10, "bonus_type": "percent", "attribute": "instant_skill_chance", "global": False, "personal": True}
        ],
"13": [
    {"level": 25, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
    {"level": 75, "bonus": 20, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
    {"level": 150, "bonus": 3, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
    {"level": 250, "bonus": 2, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
    {"level": 500, "bonus": 12, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
    {"level": 750, "bonus": 18, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
    {"level": 1000, "bonus": 70, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
    {"level": 1500, "bonus": 3, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
    {"level": 2000, "bonus": -20, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
    {"level": 2500, "bonus": 2, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
    {"level": 3000, "bonus": 36, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": False, "personal": True},
    {"level": 3500, "bonus": 2, "bonus_type": "percent", "attribute": "ultra_gold_chance", "global": True, "personal": False},
    {"level": 4000, "bonus": 175, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
    {"level": 5000, "bonus": 75, "bonus_type": "percent", "attribute": "super_gold_amount", "global": True, "personal": False},
    {"level": 6000, "bonus": 100, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
    {"level": 7500, "bonus": 1, "bonus_type": "fixed", "attribute": "battlepass_exp", "global": True, "personal": False}
],
"14": [
    {"level": 25, "bonus": 5, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
    {"level": 75, "bonus": 2, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
    {"level": 150, "bonus": 9, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
    {"level": 250, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
    {"level": 500, "bonus": 12, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
    {"level": 750, "bonus": -6, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
    {"level": 1000, "bonus": 14, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
    {"level": 1500, "bonus": 3, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
    {"level": 2000, "bonus": 4, "bonus_type": "percent", "attribute": "super_gold_chance", "global": True, "personal": False},
    {"level": 2500, "bonus": 100, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
    {"level": 3000, "bonus": 3, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
    {"level": 3500, "bonus": 42, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": True, "personal": False},
    {"level": 4000, "bonus": 20, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
    {"level": 5000, "bonus": 22, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
    {"level": 6000, "bonus": 10, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
    {"level": 7500, "bonus": 8, "bonus_type": "fixed", "attribute": "skill_power", "global": True, "personal": False}
],
      
        "15": [
        {"level": 25, "bonus": 5, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
        {"level": 75, "bonus": 1, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
        {"level": 150, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
        {"level": 250, "bonus": 40, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
        {"level": 500, "bonus": 15, "bonus_type": "percent", "attribute": "kill_gold", "global": True, "personal": False},
        {"level": 750, "bonus": 4, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
        {"level": 1000, "bonus": -16, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
        {"level": 1500, "bonus": 5, "bonus_type": "percent", "attribute": "super_exp_amount", "global": True, "personal": False},
        {"level": 2000, "bonus": 27, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
        {"level": 2500, "bonus": 20, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
        {"level": 3000, "bonus": 4, "bonus_type": "percent", "attribute": "ultra_crit_chance", "global": True, "personal": False},
        {"level": 3500, "bonus": 2, "bonus_type": "percent", "attribute": "ultra_gold_chance", "global": True, "personal": False},
        {"level": 4000, "bonus": 175, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
        {"level": 5000, "bonus": 25, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
        {"level": 6000, "bonus": 5, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
        {"level": 7500, "bonus": 20, "bonus_type": "percent", "attribute": "super_exp_amount", "global": True, "personal": False}
    ],
        "16": [
                {"level": 25, "bonus": 5, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
                {"level": 75, "bonus": -6, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
                {"level": 150, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                {"level": 250, "bonus": 10, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                {"level": 500, "bonus": 50, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                {"level": 750, "bonus": 18, "bonus_type": "percent", "attribute": "kill_gold", "global": True, "personal": False},
                {"level": 1000, "bonus": 14, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                {"level": 1500, "bonus": 6, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                {"level": 2000, "bonus": 27, "bonus_type": "percent", "attribute": "super_crit_damage", "global": True, "personal": False},
                {"level": 2500, "bonus": 10, "bonus_type": "percent", "attribute": "super_exp_amount", "global": True, "personal": False},
                {"level": 3000, "bonus": 4, "bonus_type": "percent", "attribute": "ultra_gold_chance", "global": True, "personal": False},
                {"level": 3500, "bonus": 150, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                {"level": 4000, "bonus": 3, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
                {"level": 5000, "bonus": 20, "bonus_type": "percent", "attribute": "super_crit_chance", "global": True, "personal": False},
                {"level": 6000, "bonus": 20, "bonus_type": "fixed", "attribute": "skill_power", "global": True, "personal": False},
                {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": True, "personal": False}
            ],
        "17": [
                {"level": 25, "bonus": 3, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                {"level": 75, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                {"level": 150, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                {"level": 250, "bonus": 10, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                {"level": 500, "bonus": 25, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
                {"level": 750, "bonus": 4, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
                {"level": 1000, "bonus": 70, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
                {"level": 1500, "bonus": 80, "bonus_type": "percent", "attribute": "super_crit_damage", "global": False, "personal": True},
                {"level": 2000, "bonus": 7, "bonus_type": "percent", "attribute": "super_exp_amount", "global": True, "personal": False},
                {"level": 2500, "bonus": 2, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                {"level": 3000, "bonus": 125, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                {"level": 3500, "bonus": 2, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
                {"level": 4000, "bonus": 50, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
                {"level": 5000, "bonus": 75, "bonus_type": "percent", "attribute": "super_gold_amount", "global": True, "personal": False},
                {"level": 6000, "bonus": 10, "bonus_type": "percent", "attribute": "super_crit_chance", "global": True, "personal": False},
                {"level": 7500, "bonus": 25, "bonus_type": "percent", "attribute": "goblin_gold", "global": True, "personal": False}
            ],
        "18": [
                    {"level": 25, "bonus": -1, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
                    {"level": 75, "bonus": 6, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
                    {"level": 150, "bonus": 8, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
                    {"level": 250, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                    {"level": 500, "bonus": 50, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                    {"level": 750, "bonus": 13, "bonus_type": "percent", "attribute": "range", "global": True, "personal": False},
                    {"level": 1000, "bonus": 14, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                    {"level": 1500, "bonus": 3, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                    {"level": 2000, "bonus": 4, "bonus_type": "percent", "attribute": "super_exp_chance", "global": True, "personal": False},
                    {"level": 2500, "bonus": 100, "bonus_type": "percent", "attribute": "super_gold_amount", "global": False, "personal": True},
                    {"level": 3000, "bonus": 125, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": True, "personal": False},
                    {"level": 3500, "bonus": 15, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
                    {"level": 4000, "bonus": 5, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                    {"level": 5000, "bonus": 10, "bonus_type": "percent", "attribute": "super_energy_amount", "global": True, "personal": False},
                    {"level": 6000, "bonus": 8, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                    {"level": 7500, "bonus": 25, "bonus_type": "percent", "attribute": "ultra_energy_amount", "global": True, "personal": False}
                ],
        "19": [
                        {"level": 25, "bonus": 10, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
                        {"level": 75, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                        {"level": 150, "bonus": 30, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                        {"level": 250, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                        {"level": 500, "bonus": 10, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
                        {"level": 750, "bonus": 60, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
                        {"level": 1000, "bonus": -7, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
                        {"level": 1500, "bonus": 2, "bonus_type": "percent", "attribute": "super_crit_chance", "global": True, "personal": False},
                        {"level": 2000, "bonus": 18, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                        {"level": 2500, "bonus": 6, "bonus_type": "percent", "attribute": "super_exp_chance", "global": True, "personal": False},
                        {"level": 3000, "bonus": 3, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                        {"level": 3500, "bonus": 42, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
                        {"level": 4000, "bonus": 50, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                        {"level": 5000, "bonus": 22, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                        {"level": 6000, "bonus": 8, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                        {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "super_gold_amount", "global": True, "personal": False}
                    ],
        "20": [
                            {"level": 25, "bonus": 5, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
                            {"level": 75, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                            {"level": 150, "bonus": 6, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                            {"level": 250, "bonus": 40, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
                            {"level": 500, "bonus": 50, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                            {"level": 750, "bonus": 6, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                            {"level": 1000, "bonus": 5, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                            {"level": 1500, "bonus": -18, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
                            {"level": 2000, "bonus": 27, "bonus_type": "percent", "attribute": "super_crit_damage", "global": True, "personal": False},
                            {"level": 2500, "bonus": 20, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                            {"level": 3000, "bonus": 1, "bonus_type": "percent", "attribute": "ultra_gold_chance", "global": True, "personal": False},
                            {"level": 3500, "bonus": 4, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                            {"level": 4000, "bonus": 50, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                            {"level": 5000, "bonus": 75, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
                            {"level": 6000, "bonus": 30, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
                            {"level": 7500, "bonus": 6, "bonus_type": "percent", "attribute": "ultra_crit_chance", "global": False, "personal": True}
                        ],
        "21": [
                                {"level": 25, "bonus": 5, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                                {"level": 75, "bonus": 20, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                {"level": 150, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                                {"level": 250, "bonus": 8, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                                {"level": 500, "bonus": 5, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                                {"level": 750, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                                {"level": 1000, "bonus": 5, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
                                {"level": 1500, "bonus": -18, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
                                {"level": 2000, "bonus": 27, "bonus_type": "percent", "attribute": "super_gold_amount", "global": True, "personal": False},
                                {"level": 2500, "bonus": 10, "bonus_type": "percent", "attribute": "super_crit_damage", "global": False, "personal": True},
                                {"level": 3000, "bonus": 19, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
                                {"level": 3500, "bonus": 4, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                                {"level": 4000, "bonus": 50, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                                {"level": 5000, "bonus": 75, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
                                {"level": 6000, "bonus": 250, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": False, "personal": True},
                                {"level": 7500, "bonus": 30, "bonus_type": "percent", "attribute": "super_crit_chance", "global": False, "personal": True}
                            ],
        "22": [
                                   {"level": 25, "bonus": 3, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
                                    {"level": 75, "bonus": 10, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
                                    {"level": 150, "bonus": 8, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                                    {"level": 250, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                                    {"level": 500, "bonus": 15, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
                                    {"level": 750, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                                    {"level": 1000, "bonus": 15, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
                                    {"level": 1500, "bonus": 24, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                    {"level": 2000, "bonus": 7, "bonus_type": "percent", "attribute": "super_exp_amount", "global": True, "personal": False},
                                    {"level": 2500, "bonus": 2, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                                    {"level": 3000, "bonus": 125, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": False, "personal": True},
                                    {"level": 3500, "bonus": 150, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                    {"level": 4000, "bonus": 8, "bonus_type": "percent", "attribute": "ultra_gold_chance", "global": False, "personal": True},
                                    {"level": 5000, "bonus": 20, "bonus_type": "percent", "attribute": "super_crit_chance", "global": True, "personal": False},
                                    {"level": 6000, "bonus": 80, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
                                    {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "super_crit_damage", "global": True, "personal": False}
                                ],
        "23": [
                                        {"level": 25, "bonus": -5, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
                                        {"level": 75, "bonus": 7, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                                        {"level": 150, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                                        {"level": 250, "bonus": 4, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                                        {"level": 500, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                                        {"level": 750, "bonus": 60, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
                                        {"level": 1000, "bonus": 21, "bonus_type": "percent", "attribute": "kill_gold", "global": True, "personal": False},
                                        {"level": 1500, "bonus": 40, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                                        {"level": 2000, "bonus": 27, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                                        {"level": 2500, "bonus": 6, "bonus_type": "percent", "attribute": "super_crit_chance", "global": False, "personal": True},
                                        {"level": 3000, "bonus": 19, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
                                        {"level": 3500, "bonus": 150, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                        {"level": 4000, "bonus": 175, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": False, "personal": True},
                                        {"level": 5000, "bonus": 22, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                                        {"level": 6000, "bonus": 100, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                                        {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": True, "personal": False}
                                    ],
        "24": [
                                            {"level": 25, "bonus": 1, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                                            {"level": 75, "bonus": 7, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                                            {"level": 150, "bonus": 9, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
                                            {"level": 250, "bonus": 20, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
                                            {"level": 500, "bonus": 50, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
                                            {"level": 750, "bonus": 18, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                            {"level": 1000, "bonus": -7, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
                                            {"level": 1500, "bonus": 8, "bonus_type": "percent", "attribute": "super_crit_chance", "global": False, "personal": True},
                                            {"level": 2000, "bonus": 4, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                                            {"level": 2500, "bonus": 2, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                                            {"level": 3000, "bonus": 1, "bonus_type": "percent", "attribute": "ultra_gold_chance", "global": True, "personal": False},
                                            {"level": 3500, "bonus": 150, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                            {"level": 4000, "bonus": 20, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
                                            {"level": 5000, "bonus": 75, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
                                            {"level": 6000, "bonus": 20, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                                            {"level": 7500, "bonus": 10, "bonus_type": "percent", "attribute": "instant_skill_chance", "global": False, "personal": True}
                                        ],
        "25": [
                {"level": 25, "bonus": 10, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
                {"level": 75, "bonus": 2, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                {"level": 150, "bonus": -8, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
                {"level": 250, "bonus": 2, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
                {"level": 500, "bonus": 3, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                {"level": 750, "bonus": 60, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
                {"level": 1000, "bonus": 70, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                {"level": 1500, "bonus": 17, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                {"level": 2000, "bonus": 18, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                {"level": 2500, "bonus": 5, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                {"level": 3000, "bonus": 125, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
                {"level": 3500, "bonus": 2, "bonus_type": "percent", "attribute": "ultra_crit_chance", "global": True, "personal": False},
                {"level": 4000, "bonus": 50, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                {"level": 5000, "bonus": 4, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                {"level": 6000, "bonus": 100, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
                {"level": 7500, "bonus": 300, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": False, "personal": True}
            ],
        "26": [
                {"level": 25, "bonus": 3, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
                {"level": 75, "bonus": 2, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                {"level": 150, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                {"level": 250, "bonus": 10, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
                {"level": 500, "bonus": -5, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
                {"level": 750, "bonus": 13, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                {"level": 1000, "bonus": 21, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                {"level": 1500, "bonus": 3, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                {"level": 2000, "bonus": 1, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                {"level": 2500, "bonus": 16, "bonus_type": "percent", "attribute": "super_gold_chance", "global": False, "personal": True},
                {"level": 3000, "bonus": 125, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": False, "personal": True},
                {"level": 3500, "bonus": 150, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                {"level": 4000, "bonus": 3, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
                {"level": 5000, "bonus": 75, "bonus_type": "percent", "attribute": "super_gold_amount", "global": False, "personal": True},
                {"level": 6000, "bonus": 25, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "super_crit_damage", "global": True, "personal": False}
            ],
        "27": [
                    {"level": 25, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                    {"level": 75, "bonus": 20, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
                    {"level": 150, "bonus": 3, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                    {"level": 250, "bonus": 2, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
                    {"level": 500, "bonus": 12, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                    {"level": 750, "bonus": -14, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
                    {"level": 1000, "bonus": 70, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
                    {"level": 1500, "bonus": 80, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                    {"level": 2000, "bonus": 18, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                    {"level": 2500, "bonus": 5, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                    {"level": 3000, "bonus": 3, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                    {"level": 3500, "bonus": 2, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
                    {"level": 4000, "bonus": 50, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": True, "personal": False},
                    {"level": 5000, "bonus": 12, "bonus_type": "percent", "attribute": "super_exp_amount", "global": True, "personal": False},
                    {"level": 6000, "bonus": 5, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
                    {"level": 7500, "bonus": 10, "bonus_type": "percent", "attribute": "instant_skill_chance", "global": False, "personal": True}
                ],
        "28": [
                {"level": 25, "bonus": 2, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                {"level": 75, "bonus": 20, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                {"level": 150, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                {"level": 250, "bonus": 12, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
                {"level": 500, "bonus": 5, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                {"level": 750, "bonus": -14, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
                {"level": 1000, "bonus": 15, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                {"level": 1500, "bonus": 8, "bonus_type": "percent", "attribute": "super_gold_chance", "global": False, "personal": True},
                {"level": 2000, "bonus": 7, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                {"level": 2500, "bonus": 16, "bonus_type": "percent", "attribute": "super_crit_chance", "global": False, "personal": True},
                {"level": 3000, "bonus": 36, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                {"level": 3500, "bonus": 42, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": False, "personal": True},
                {"level": 4000, "bonus": 20, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
                {"level": 5000, "bonus": 12, "bonus_type": "percent", "attribute": "super_exp_amount", "global": True, "personal": False},
                {"level": 6000, "bonus": 100, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                {"level": 7500, "bonus": 10, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False}
            ],
        "29": [
                    {"level": 25, "bonus": 1, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                    {"level": 25, "bonus": 8, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                    {"level": 75, "bonus": 20, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                    {"level": 150, "bonus": 2, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
                    {"level": 250, "bonus": 15, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                    {"level": 500, "bonus": 50, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
                    {"level": 750, "bonus": 4, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                    {"level": 1000, "bonus": 15, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                    {"level": 1500, "bonus": -8, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
                    {"level": 2000, "bonus": 4, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                    {"level": 2500, "bonus": 30, "bonus_type": "percent", "attribute": "super_gold_amount", "global": True, "personal": False},
                    {"level": 3000, "bonus": 3, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                    {"level": 3500, "bonus": 6, "bonus_type": "percent", "attribute": "ultra_crit_chance", "global": False, "personal": True},
                    {"level": 4000, "bonus": 1, "bonus_type": "percent", "attribute": "ultra_energy_chance", "global": True, "personal": False},
                    {"level": 5000, "bonus": 8, "bonus_type": "percent", "attribute": "super_crit_chance", "global": False, "personal": True},
                    {"level": 6000, "bonus": 15, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
                    {"level": 7500, "bonus": 25, "bonus_type": "percent", "attribute": "ultra_energy_amount", "global": True, "personal": False}
                ],
        "30": [
                        {"level": 25, "bonus": 3, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                        {"level": 75, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                        {"level": 150, "bonus": -3, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
                        {"level": 250, "bonus": 10, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                        {"level": 500, "bonus": 12, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
                        {"level": 750, "bonus": 18, "bonus_type": "percent", "attribute": "kill_gold", "global": True, "personal": False},
                        {"level": 1000, "bonus": 5, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                        {"level": 1500, "bonus": 40, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
                        {"level": 2000, "bonus": 27, "bonus_type": "percent", "attribute": "super_crit_damage", "global": True, "personal": False},
                        {"level": 2500, "bonus": 10, "bonus_type": "percent", "attribute": "super_exp_amount", "global": True, "personal": False},
                        {"level": 3000, "bonus": 125, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                        {"level": 3500, "bonus": 42, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": False, "personal": True},
                        {"level": 4000, "bonus": 3, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
                        {"level": 5000, "bonus": 200, "bonus_type": "percent", "attribute": "super_gold_amount", "global": True, "personal": False},
                        {"level": 6000, "bonus": 20, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                        {"level": 7500, "bonus": 300, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False}
                    ],
        "31": [
                            {"level": 25, "bonus": 5, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                            {"level": 75, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                            {"level": 150, "bonus": 6, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                            {"level": 250, "bonus": -4, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
                            {"level": 500, "bonus": 50, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
                            {"level": 750, "bonus": 60, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
                            {"level": 1000, "bonus": 5, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
                            {"level": 1500, "bonus": 3, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                            {"level": 2000, "bonus": 90, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                            {"level": 2500, "bonus": 10, "bonus_type": "percent", "attribute": "super_exp_amount", "global": True, "personal": False},
                            {"level": 3000, "bonus": 36, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": True, "personal": False},
                            {"level": 3500, "bonus": 42, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                            {"level": 4000, "bonus": 8, "bonus_type": "percent", "attribute": "ultra_gold_chance", "global": False, "personal": True},
                            {"level": 5000, "bonus": 4, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
                            {"level": 6000, "bonus": 8, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                            {"level": 7500, "bonus": 25, "bonus_type": "fixed", "attribute": "skill_power", "global": True, "personal": False}
                        ],
        "32": [
                                {"level": 25, "bonus": 5, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                                {"level": 75, "bonus": 10, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
                                {"level": 150, "bonus": -8, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
                                {"level": 250, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                                {"level": 500, "bonus": 5, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                                {"level": 750, "bonus": 18, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                                {"level": 1000, "bonus": 15, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
                                {"level": 1500, "bonus": 2, "bonus_type": "percent", "attribute": "super_gold_chance", "global": True, "personal": False},
                                {"level": 2000, "bonus": 7, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                                {"level": 2500, "bonus": 30, "bonus_type": "percent", "attribute": "super_crit_damage", "global": True, "personal": False},
                                {"level": 3000, "bonus": 10, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
                                {"level": 3500, "bonus": 150, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                {"level": 4000, "bonus": 5, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                                {"level": 5000, "bonus": 22, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
                                {"level": 6000, "bonus": 100, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
                                {"level": 7500, "bonus": 8, "bonus_type": "percent", "attribute": "range", "global": True, "personal": False}
                            ],
        "33": [
                                    {"level": 25, "bonus": 2, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                                    {"level": 75, "bonus": 1, "bonus_type": "percent", "attribute": "crit_chance", "global": True, "personal": False},
                                    {"level": 150, "bonus": 30, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                    {"level": 250, "bonus": 12, "bonus_type": "percent", "attribute": "kill_gold", "global": True, "personal": False},
                                    {"level": 500, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                                    {"level": 750, "bonus": 60, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
                                    {"level": 1000, "bonus": 8, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                                    {"level": 1500, "bonus": 17, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                                    {"level": 2000, "bonus": 7, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                                    {"level": 2500, "bonus": -22, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
                                    {"level": 3000, "bonus": 36, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                    {"level": 3500, "bonus": 2, "bonus_type": "percent", "attribute": "ultra_crit_chance", "global": True, "personal": False},
                                    {"level": 4000, "bonus": 175, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": False, "personal": True},
                                    {"level": 5000, "bonus": 6, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                                    {"level": 6000, "bonus": 3, "bonus_type": "percent", "attribute": "ultra_energy_chance", "global": True, "personal": False},
                                    {"level": 7500, "bonus": 15, "bonus_type": "percent", "attribute": "power_mage_energy", "global": True, "personal": False}
                                ],
        "34": [
                                        {"level": 25, "bonus": -1, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
                                        {"level": 75, "bonus": 7, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                                        {"level": 150, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                                        {"level": 250, "bonus": 12, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
                                        {"level": 500, "bonus": 12, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
                                        {"level": 750, "bonus": 30, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
                                        {"level": 1000, "bonus": 8, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                                        {"level": 1500, "bonus": 3, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                                        {"level": 2000, "bonus": 27, "bonus_type": "percent", "attribute": "super_gold_amount", "global": True, "personal": False},
                                        {"level": 2500, "bonus": 30, "bonus_type": "percent", "attribute": "super_crit_damage", "global": False, "personal": True},
                                        {"level": 3000, "bonus": 125, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                        {"level": 3500, "bonus": 4, "bonus_type": "fixed", "attribute": "energy_income", "global": True, "personal": False},
                                        {"level": 4000, "bonus": 3, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
                                        {"level": 5000, "bonus": 25, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
                                        {"level": 6000, "bonus": 25, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                                        {"level": 7500, "bonus": 30, "bonus_type": "percent", "attribute": "super_crit_chance", "global": True, "personal": False}
                                    ],
        "35": [
                                            {"level": 25, "bonus": 10, "bonus_type": "percent", "attribute": "crit_damage", "global": False, "personal": True},
                                            {"level": 75, "bonus": 20, "bonus_type": "percent", "attribute": "kill_gold", "global": False, "personal": True},
                                            {"level": 150, "bonus": 8, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                                            {"level": 250, "bonus": 2, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                                            {"level": 500, "bonus": 10, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
                                            {"level": 750, "bonus": 6, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
                                            {"level": 1000, "bonus": 3, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                                            {"level": 1500, "bonus": 80, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                            {"level": 2000, "bonus": 4, "bonus_type": "percent", "attribute": "super_crit_chance", "global": True, "personal": False},
                                            {"level": 2500, "bonus": -22, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
                                            {"level": 3000, "bonus": 36, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                            {"level": 3500, "bonus": 2, "bonus_type": "percent", "attribute": "ultra_gold_chance", "global": True, "personal": False},
                                            {"level": 4000, "bonus": 7, "bonus_type": "percent", "attribute": "super_exp_chance", "global": True, "personal": False},
                                            {"level": 5000, "bonus": 75, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
                                            {"level": 6000, "bonus": 5, "bonus_type": "percent", "attribute": "ultra_exp_chance", "global": True, "personal": False},
                                            {"level": 7500, "bonus": 8, "bonus_type": "fixed", "attribute": "skill_power", "global": True, "personal": False}
                                        ],
        "36": [
                                                {"level": 25, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
                                                {"level": 75, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
                                                {"level": 150, "bonus": 9, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
                                                {"level": 250, "bonus": -4, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
                                                {"level": 500, "bonus": 25, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
                                                {"level": 750, "bonus": 13, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
                                                {"level": 1000, "bonus": 15, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
                                                {"level": 1500, "bonus": 8, "bonus_type": "percent", "attribute": "super_gold_chance", "global": False, "personal": True},
                                                {"level": 2000, "bonus": 7, "bonus_type": "percent", "attribute": "super_exp_amount", "global": True, "personal": False},
                                                {"level": 2500, "bonus": 30, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                                {"level": 3000, "bonus": 10, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
                                                {"level": 3500, "bonus": 150, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
                                                {"level": 4000, "bonus": 175, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": False, "personal": True},
                                                {"level": 5000, "bonus": 65, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
                                                {"level": 6000, "bonus": 25, "bonus_type": "percent", "attribute": "super_crit_chance", "global": False, "personal": True},
                                                {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "super_crit_damage", "global": True, "personal": False}
                                            ],
    }

@app.route("/", methods=["GET"])
def index():
    return send_file("levelup_table.html")

if __name__ == "__main__":
    app.run(debug=True)
