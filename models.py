import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

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
