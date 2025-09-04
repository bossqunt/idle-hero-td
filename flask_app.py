from flask import Flask, jsonify, send_file

app = Flask(__name__)

# Route to serve the levelup_table.html front-end
@app.route("/levelup-table", methods=["GET"])
def serve_levelup_html():
    return send_file("levelup_table.html")

@app.route("/levelup", methods=["GET"])
def level_up():
    # Monster names (example, update as needed)
    monster_names = {
        "1": "Monster 1",
        "2": "Monster 2",
        "3": "Monster 3",
        "4": "Monster 4",
        "5": "Monster 5",
        "6": "Monster 6",
        "7": "Monster 7",
        "8": "Monster 8",
        "9": "Monster 9",
        "10": "Monster 10",
        "11": "Monster 11"
    }

    # Levels to show as columns
    levels = [25, 75, 150, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 6000, 7500]

    # Monster data (copy your previous data here)
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
            {"level": 25, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 75, "bonus": 6, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
            {"level": 150, "bonus": 9, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 250, "bonus": 4, "bonus_type": "fixed", "attribute": "rank_exp", "global": True, "personal": False},
            {"level": 500, "bonus": 15, "bonus_type": "percent", "attribute": "kill_gold", "global": True, "personal": False},
            {"level": 750, "bonus": 30, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
            {"level": 1000, "bonus": -16, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
            {"level": 1500, "bonus": 8, "bonus_type": "percent", "attribute": "super_crit_chance", "global": False, "personal": True},
            {"level": 2000, "bonus": 18, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
            {"level": 2500, "bonus": 30, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 3000, "bonus": 125, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
            {"level": 3500, "bonus": 15, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
            {"level": 4000, "bonus": 175, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": False, "personal": True},
            {"level": 5000, "bonus": 75, "bonus_type": "percent", "attribute": "ultra_gold_amount", "global": True, "personal": False},
            {"level": 6000, "bonus": 25, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
            {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": True, "personal": False}
        ],
        "8": [
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
        "9": [
            {"level": 25, "bonus": 1, "bonus_type": "fixed", "attribute": "skill_power", "global": False, "personal": True},
            {"level": 75, "bonus": 6, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 150, "bonus": 8, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
            {"level": 250, "bonus": -4, "bonus_type": "percent", "attribute": "skill_cooldown", "global": True, "personal": False},
            {"level": 500, "bonus": 25, "bonus_type": "percent", "attribute": "attack_speed", "global": False, "personal": True},
            {"level": 750, "bonus": 13, "bonus_type": "percent", "attribute": "range", "global": False, "personal": True},
            {"level": 1000, "bonus": 21, "bonus_type": "percent", "attribute": "crit_damage", "global": True, "personal": False},
            {"level": 1500, "bonus": 24, "bonus_type": "percent", "attribute": "super_gold_amount", "global": True, "personal": False},
            {"level": 2000, "bonus": 4, "bonus_type": "percent", "attribute": "super_exp_chance", "global": True, "personal": False},
            {"level": 2500, "bonus": 8, "bonus_type": "fixed", "attribute": "skill_duration", "global": False, "personal": True},
            {"level": 3000, "bonus": 4, "bonus_type": "percent", "attribute": "ultra_crit_chance", "global": True, "personal": False},
            {"level": 3500, "bonus": 42, "bonus_type": "percent", "attribute": "damage", "global": True, "personal": False},
            {"level": 4000, "bonus": 20, "bonus_type": "percent", "attribute": "ultra_exp_amount", "global": True, "personal": False},
            {"level": 5000, "bonus": -25, "bonus_type": "percent", "attribute": "skill_cooldown", "global": False, "personal": True},
            {"level": 6000, "bonus": 250, "bonus_type": "percent", "attribute": "damage", "global": False, "personal": True},
            {"level": 7500, "bonus": 125, "bonus_type": "percent", "attribute": "ultra_crit_damage", "global": True, "personal": False}
        ],
        "10": [
            {"level": 25, "bonus": 2, "bonus_type": "percent", "attribute": "attack_speed", "global": True, "personal": False},
            {"level": 75, "bonus": 1, "bonus_type": "percent", "attribute": "crit_chance", "global": False, "personal": True},
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
            {"level": 7500, "bonus": 12, "bonus_type": "percent", "attribute": "super_crit_chance", "global": False, "personal": True}
        ],
        "11": [
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
        ]
    }
    


    # Define hero_list globally so it can be reused in all endpoints
    hero_list = [
        {"id": 1, "name": "Militia", "skill": "Arcane Blast", "cd": 8, "description": "Unleashes a burst of arcane energy, dealing AoE damage.", "value": 120, "time": 5},
        {"id": 2, "name": "Apprentice", "skill": "Shield Slam", "cd": 10, "description": "Stuns an enemy and reduces incoming damage for 3s.", "value": 80, "time": 3},
        {"id": 3, "name": "Scout", "skill": "Nature’s Grasp", "cd": 12, "description": "Roots enemies in place while healing nearby allies.", "value": 60, "time": 4},
        {"id": 4, "name": "Viking", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
        {"id": 5, "name": "Druid", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
        {"id": 6, "name": "Hunter", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
        {"id": 7, "name": "Ninja", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
        {"id": 8, "name": "Sorcerer", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
        {"id": 9, "name": "Forester", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
        {"id": 10, "name": "Assassin", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6},
        {"id": 11, "name": "Witch", "skill": "Thunder Strike", "cd": 7, "description": "Calls down lightning, striking up to 3 random enemies.", "value": 95, "time": 6}
    ]

    hero_names = {str(hero["id"]): hero["name"] for hero in hero_list}

    table = []
    for monster_id, bonuses in monster_data.items():
        row = {"monster": hero_names.get(monster_id, monster_id)}
        for lvl in levels:
            bonus_str = ""
            for entry in bonuses:
                if entry["level"] == lvl:
                    sign = "+" if entry["bonus"] >= 0 else ""
                    bonus_str = f"{sign}{entry['bonus']} {entry['attribute'].replace('_', ' ').title()}"
                    if entry["bonus_type"] == "percent":
                        bonus_str += "%"
                    break
            row[f"level {lvl}"] = bonus_str
        table.append(row)

    columns = ["monster"] + [f"level {lvl}" for lvl in levels]
    return jsonify({"table": table, "columns": columns})


@app.route("/synergy", methods=["GET"])
def synergy():
    response = {
        "status": "success",
        "data": {
            "tier": 2,
            "hero": [101, 104, 109, 113],
            "rank": 1,
            "global": True,
            "personal": False
        }
    }
    return jsonify(response)


@app.route("/heroes", methods=["GET"])
def heroes():
    response = {
        "status": "success",
        "data": [
            {
                "id": 1,
                "name": "Militia",
                "skill": "Arcane Blast",
                "cd": 8,
                "description": "Unleashes a burst of arcane energy, dealing AoE damage.",
                "value": 120,
                "time": 5
            },
            {
                "id": 2,
                "name": "Apprentice",
                "skill": "Shield Slam",
                "cd": 10,
                "description": "Stuns an enemy and reduces incoming damage for 3s.",
                "value": 80,
                "time": 3
            },
            {
                "id": 3,
                "name": "Scout",
                "skill": "Nature’s Grasp",
                "cd": 12,
                "description": "Roots enemies in place while healing nearby allies.",
                "value": 60,
                "time": 4
            },
            {
                "id": 4,
                "name": "Viking",
                "skill": "Thunder Strike",
                "cd": 7,
                "description": "Calls down lightning, striking up to 3 random enemies.",
                "value": 95,
                "time": 6
            },
            {
                "id": 5,
                "name": "Druid",
                "skill": "Thunder Strike",
                "cd": 7,
                "description": "Calls down lightning, striking up to 3 random enemies.",
                "value": 95,
                "time": 6
            },
            {
                "id": 6,
                "name": "Hunter",
                "skill": "Thunder Strike",
                "cd": 7,
                "description": "Calls down lightning, striking up to 3 random enemies.",
                "value": 95,
                "time": 6
            },
            {
                "id": 7,
                "name": "Ninja",
                "skill": "Thunder Strike",
                "cd": 7,
                "description": "Calls down lightning, striking up to 3 random enemies.",
                "value": 95,
                "time": 6
            },
            {
                "id": 8,
                "name": "Sorcerer",
                "skill": "Thunder Strike",
                "cd": 7,
                "description": "Calls down lightning, striking up to 3 random enemies.",
                "value": 95,
                "time": 6
            },
            {
                "id": 9,
                "name": "Forester",
                "skill": "Thunder Strike",
                "cd": 7,
                "description": "Calls down lightning, striking up to 3 random enemies.",
                "value": 95,
                "time": 6
            },
            {
                "id": 10,
                "name": "Assassin",
                "skill": "Thunder Strike",
                "cd": 7,
                "description": "Calls down lightning, striking up to 3 random enemies.",
                "value": 95,
                "time": 6
            },
            {
                "id": 11,
                "name": "Witch",
                "skill": "Thunder Strike",
                "cd": 7,
                "description": "Calls down lightning, striking up to 3 random enemies.",
                "value": 95,
                "time": 6
            }
        ],
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
