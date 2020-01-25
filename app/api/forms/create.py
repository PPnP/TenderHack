from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField, SelectField, SubmitField
from wtforms.validators import DataRequired

from app.api.models.request import Request


class CreateRequestForm(FlaskForm):
    category = SelectField(label='category', choices=Request.get_all_categories(),
                           validators=[DataRequired(message='This is a required field')])
    goods = StringField(label='goods', validators=[DataRequired(message='This is a required field')])
    quantity = IntegerField(label='quantity', validators=[DataRequired(message='This is a required field')])
    waiting_period = DateTimeField(label='waiting_period', validators=[DataRequired(message='This is a required field')])
    delivery_date = DateTimeField(label='delivery_date', validators=[DataRequired(message='This is a required field')])
    address = StringField(label='address', validators=[DataRequired(message='This is a required field')])
    submit = SubmitField('Create')
