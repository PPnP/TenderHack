from flask import render_template, redirect
from flask_wtf import FlaskForm

from app.api.controllers.base import BaseController
from app.api.forms.create import CreateRequestForm
from app.api.models.request import Request
from app.api.models.customer import Customer
from app.api.models.customer_to_request import CustomerRequest


class CreateRequestController(BaseController):
    action = '/create'

    def get(self):
        return render_template('create.html', form=self.get_form(), action=self.action)

    def get_form(self) -> FlaskForm:
        return CreateRequestForm()

    def process(self, form: FlaskForm):
        c = Customer.create(location=form.address)
        r = Request.create(category=form.category, goods=form.goods, quantity=form.quantity,
                           waiting_period=form.waiting_period, delivery_date=form.delivery_date)
        CustomerRequest.create(customer=c, request=r)
        return render_template('success.html')
