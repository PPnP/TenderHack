from flask import render_template, redirect
from flask.views import MethodView
from datetime import datetime

from app.api.models.request import Request
from app.api.models.customer import Customer
from app.api.models.customer_to_request import CustomerRequest
from app.api.forms.join import JoinForm


class DetailsController(MethodView):
    action = '/details/'

    def get(self, id):
        query = Request.get(Request.id == id)
        months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        request = {
            'id': query.id,
            'category': query.category,
            'goods': query.goods,
            'picture': query.picture,
            'quantity': query.quantity,
            'waiting_period': query.waiting_period.day - datetime.today().day,
            'delivery_date': {
                'day': query.delivery_date.day,
                'month': months[query.delivery_date.month - 1],
            },
            'notes': query.notes
        }
        return render_template('details.html', form=JoinForm(), request=request, id=id, action=self.action + id)

    def post(self, id):
        form = JoinForm()
        if form.validate():
            c = Customer.create(region=form.region.data)
            r = Request.get(Request.id == id)
            CustomerRequest.create(customer=c, request=r)
            return redirect('/catalog')
        request = Request.get(Request.id == id)
        return render_template('details.html', form=JoinForm(), request=request, id=id, action=self.action + id)