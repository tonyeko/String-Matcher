from flask_wtf import FlaskForm
from wtforms import StringField, MultipleFileField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    folder = MultipleFileField('File(s)', validators=[DataRequired()])
    keyword = StringField('Keyword', validators=[DataRequired()])
    submit = SubmitField('Submit')