from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from ..models import Verb

@main.route('/')
def instructions():
    return render_template('instructions.html')

@main.route('/quiz', methods=['GET', 'POST'])
def quiz():
    form = AnswerForm()
    if form.validate_on_submit():

        return redirect(url_for('.results'))

@main.route('/results')
def evaluate():
    score = 0
