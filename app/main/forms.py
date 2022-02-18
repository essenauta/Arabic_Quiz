from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from ..models import Faala

class AnswerForm(FlaskForm):
    AlMasdar = StringField('المصدر')
    AsmaAlFail = StringField('أسماء الفاع')
    AsmaAlMafoul = StringField('أسماء المفعول')
    AlMadi = StringField('الماضي')
    AlMudaria = StringField('المضارع')
    AlAmr = StringField('الأمر')
    English = StringField('English')
    submit = SubmitField('Submit')
