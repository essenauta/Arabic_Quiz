from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from ..models import Faala
from random import randrange
from .forms import AnswerForm

@main.route('/')
def instructions():
    faala=Faala.query.filter_by(id=randrange(Faala.query.count())).first()
    return render_template('instructions.html', question_id=faala.id)

@main.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz(question_id):
    faala=Faala.query.filter_by(id=question_id).first()
    formAnswer = AnswerForm()
    if formAnswer.validate_on_submit():
        return redirect(url_for('main.evaluation', question_id=question_id, al_masdar=formAnswer.AlMasdar.data.strip(), isma_al_fael=formAnswer.AsmaAlFail.data.strip(), isma_al_mafoul=formAnswer.AsmaAlMafoul.data.strip(), al_madi=formAnswer.AlMadi.data.strip(), al_mudarie=formAnswer.AlMudaria.data.strip(), al_amr=formAnswer.AlAmr.data.strip(), english=formAnswer.English.data.strip()))
    return render_template('question.html', faala=faala, formAnswer=formAnswer)

@main.route('/evaluation/<int:question_id>/<string:al_masdar>/<string:isma_al_fael>/<string:isma_al_mafoul>/<string:al_madi>/<string:al_mudarie>/<string:al_amr>/<string:english>/')
def evaluation(question_id, al_masdar, isma_al_fael, isma_al_mafoul, al_madi, al_mudarie, al_amr, english):
    score=0
    faala=Faala.query.filter_by(id=question_id).first()
    if faala.al_masdar.strip() == al_masdar:
        score+=1
    if faala.isma_al_fael.strip() == isma_al_fael:
        score+=1
    if faala.isma_al_mafoul.strip() == isma_al_mafoul:
        score+=1
    if faala.al_madi.strip() == al_madi:
        score+=1
    if faala.al_mudarie.strip() == al_mudarie:
        score+=1
    if faala.al_amr.strip() == al_amr:
        score+=1
    if faala.english.strip() == english:
        score+=1
    return render_template('evaluation.html', score=score, al_masdar_correct=faala.al_masdar.strip(), al_masdar_answer=al_masdar, isma_al_fael_correct=faala.isma_al_fael.strip(), isma_al_fael_answer=isma_al_fael, isma_al_mafoul_correct=faala.isma_al_mafoul.strip(), isma_al_mafoul_answer=isma_al_mafoul, al_madi_correct=faala.al_madi.strip(), al_madi_answer=al_madi, al_mudarie_correct=faala.al_mudarie.strip(), al_mudarie_answer=al_mudarie, al_amr_correct=faala.al_amr.strip(), al_amr_answer=al_amr, english_correct=faala.english.strip(), english_answer=english)
