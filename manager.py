import os
from app import create_app, db
from app.models import Faala

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

def make_shell_context():
    return dict(app=app, db=db, Faala=Faala)
