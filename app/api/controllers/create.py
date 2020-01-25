from flask import render_template, redirect
from flask_wtf import FlaskForm

from app.api.controllers.base import BaseController
from app.api.forms.create import CreateRequestForm
from app.api.models.request import Request



class CreateRequestController(BaseController):
    action = '/create'

    def get(self):
        return render_template('create.html', form=self.get_form(), action=self.action)

    def get_form(self) -> FlaskForm:
        return CreateRequestForm()

    def process(self, form: FlaskForm):
        Request.create(category=form.category, goods=form.goods, quantity=form.quantity,
                       waiting_period=form.waiting_period, delivery_date=form.delivery_date)
        return redirect('/catalog')
