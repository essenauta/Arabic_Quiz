from . import db
from flask import current_app

class Faala(db.Model):
    __tablename__ = 'faala'
    id = db.Column(db.Integer, primary_key=True)
    form = db.Column(db.String(12), nullable=False)
    root= db.Column(db.String(10), nullable=False)
    alMasdar = db.Column(db.String(24), nullable=False)
    asmaAlFail = db.Column(db.String(24), nullable=False)
    asmaAlMafoul = db.Column(db.String(24), nullable=False)
    alMadi = db.Column(db.String(24), nullable=False)
    alMudaria = db.Column(db.String(24), nullable=False)
    alAmr = db.Column(db.String(24), nullable=False)
    english = db.Column(db.String(24), nullable=False)
