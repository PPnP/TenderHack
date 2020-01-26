from flask.views import MethodView
from flask import render_template
from datetime import datetime

from app.api.models.request import Request
from app.api.models.customer_to_request import CustomerRequest


class SupplierController(MethodView):
    def get(self):
        customers = [
            {
                'id': '1',
                'name': 'ЛИТ 1533',
                'address': '15-я Парковая, 16к3'
            },
            {
                'id': '2',
                'name': 'НИУ ВШЭ',
                'address': 'Кременчугская, 5/3'
            },
            {
                'id': '3',
                'name': 'ЛИТ 1533',
                'address': 'Ломоносовский, 16'
            },
            {
                'id': '4',
                'name': 'ЛИТ 1533',
                'address': 'Ломоносовский, 16'
            }
        ]
        return render_template('supplier.html', customers=customers)
