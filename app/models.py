from . import db
from flask import current_app

class Faala(db.Model):
    __tablename__ = 'verbs'
    id = db.Column(db.Integer, primary_key=True)
    form = db.Column(db.String(12), nullable=False)
    al_jidhr= db.Column(db.String(10), nullable=False)
    al_masdar = db.Column(db.String(24), nullable=False)
    isma_al_fael = db.Column(db.String(24), nullable=False)
    isma_al_mafoul = db.Column(db.String(24), nullable=False)
    al_madi = db.Column(db.String(24), nullable=False)
    al_mudarie = db.Column(db.String(24), nullable=False)
    al_amr = db.Column(db.String(24), nullable=False)
    english = db.Column(db.String(24), nullable=False)
