from flask import render_template
from flask_wtf import FlaskForm
from datetime import datetime

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
        date = form.waiting_period.data.split('-')
        year, month, day = int(date[0]), int(date[1]), int(date[2])
        waiting_period = datetime(year=year, month=month, day=day)
        date = form.delivery_date.data.split('-')
        year, month, day = int(date[0]), int(date[1]), int(date[2])
        delivery_date = datetime(year=year, month=month, day=day)
        r = Request.create(category=form.category.data, goods=form.goods.data, quantity=form.quantity.data,
                           waiting_period=waiting_period, delivery_date=delivery_date)
        c = Customer.create(address=form.region.data)
        CustomerRequest.create(customer=c, request=r)
        return render_template('success.html')
