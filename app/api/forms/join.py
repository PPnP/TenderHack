from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class JoinForm(FlaskForm):
    address = StringField(label='address', validators=[DataRequired(message='This is a required field')])
    submit = SubmitField('Join')
