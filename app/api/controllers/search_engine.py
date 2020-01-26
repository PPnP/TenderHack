from flask.views import MethodView
from flask import render_template
from datetime import datetime

from app.api.models.request import Request


class SearchEngineController(MethodView):
    def get(self, flag):
        query = Request.select()
        requests = list()
        for q in query:
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
        # if flag == '1':
        #     pass
        return render_template('search.html', requests=requests)
