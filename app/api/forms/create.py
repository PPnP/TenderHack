from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

from app.api.models.request import Request


class CreateRequestForm(FlaskForm):
    category = SelectField(label='category', choices=Request.get_all_categories(),
                           validators=[DataRequired(message='This is a required field')])
    goods = StringField(label='goods', validators=[DataRequired(message='This is a required field')])
    quantity = IntegerField(label='quantity', validators=[DataRequired(message='This is a required field')])
    waiting_period = StringField(label='waiting_period', validators=[DataRequired(message='This is a required field')])
    delivery_date = StringField(label='delivery_date', validators=[DataRequired(message='This is a required field')])
    region = StringField(label='address', validators=[DataRequired(message='This is a required field')])
    notes = TextAreaField(label='notes', validators=[DataRequired(message='This is a required field')])
    submit = SubmitField('Create')
