from flask.views import MethodView
from flask import render_template, redirect

from app.api.models.request import Request
from app.api.models.customer import Customer
from app.api.models.customer_to_request import CustomerRequest
from app.api.forms.join import JoinForm


class DetailsController(MethodView):
    action = '/details/'

    def get(self, id):
        request = Request.get(Request.id == id)
        return render_template('details.html', request=request, id=id, action=self.action + id)

    def post(self, id):
        form = JoinForm()
        if form.validate():
            c = Customer.create(location=form.region.data)
            r = Request.get(Request.id == id)
            CustomerRequest.create(customer=c, request=r)
            return redirect('/')
        return render_template('details.html')
