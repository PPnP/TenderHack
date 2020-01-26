from flask.views import MethodView
from flask import render_template

from app.api.models.request import Request
from datetime import datetime


class CatalogController(MethodView):
    def get(self):
        query = Request.select()
        requests = list()
        for q in query:
            if not q.is_completed:
                months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                          'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
                requests.append({
                    'id': q.id,
                    'category': q.category,
                    'goods': q.goods,
                    'picture': q.picture,
                    'quantity': q.quantity,
                    'waiting_period': q.waiting_period.day - datetime.today().day,
                    'delivery_date': {
                        'day': q.delivery_date.day,
                        'month': months[q.delivery_date.month - 1],
                    },
                    'notes': q.notes
                })
        return render_template('catalog.html', requests=requests, categories=Request.get_all_categories())
