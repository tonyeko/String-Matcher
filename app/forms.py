from flask_wtf import FlaskForm
from wtforms import StringField, MultipleFileField, SubmitField, RadioField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    folder = MultipleFileField('File(s)', validators=[DataRequired()])
    keyword = StringField('Keyword', validators=[DataRequired()])
    algo = RadioField('Algorithm', choices=[('kmp','Knuth-Morris-Pratt'),('bm','Boyer-Moore'),('regex','Regular Expression')])
    submit = SubmitField('Submit')