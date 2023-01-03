from flask import Flask, request, render_template, url_for
import os
import csv
import random
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/')
def instructions():
    return render_template('instructions.html')

@app.route('/quiz')
def quiz():
    global word_dict
    word_dict, verb_form = generate_word()
    return render_template('question.html',root=word_dict['الجذر'],verb_form=verb_form)

@app.route('/results')
def evaluate():
    score = 0
    almasdar = request.args['almasdar']
    fael = request.args['fael']
    mafeul = request.args['mafeul']
    almadi = request.args['almadi']
    almudarie = request.args['almudarie']
    alamr = request.args['alamr']
    English = request.args['English']

    if almasdar == word_dict['المصدر']:
        score += 1
    if fael == word_dict['أسماء الفاعل']:
        score += 1
    if mafeul == word_dict['أسماء المفعول']:
        score += 1
    if almadi == word_dict['الماضي']:
        score += 1
    if almudarie == word_dict['الْمُضَارِع']:
        score += 1
    if alamr == word_dict['الْأَمْر']:
        score += 1
    if English == word_dict['English']:
        score += 1

    if score == 7:
        msg = 'ممتاز'
    else:
        msg = 'حاول مرة أخرى'

    return render_template('evaluation.html', msg=msg, answers_correct=score, answer1=almasdar, answer2=fael, answer3=mafeul, answer4=almadi, answer5=almudarie, answer6=alamr, answer7=English, correct1=word_dict['المصدر'], correct2=word_dict['أسماء الفاعل'], correct3=word_dict['أسماء المفعول'], correct4=word_dict['الماضي'], correct5=word_dict['الْمُضَارِع'], correct6=word_dict['الْأَمْر'], correct7=word_dict['English'])
