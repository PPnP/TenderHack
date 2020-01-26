from flask.views import MethodView
from flask import render_template

from app.api.models.request import Request


class SearchEngineController(MethodView):
    def get(self, flag):
        requests = Request.select()
        # if flag == '1':
        #     pass
        return render_template('search.html', requests=requests)
