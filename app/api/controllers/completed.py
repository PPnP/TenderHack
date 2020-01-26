from flask.views import MethodView
from flask import render_template

from app.api.models.request import Request


class CompletedController(MethodView):
    def get(self):
        requests = Request.select().where(Request.is_completed == True)
        return render_template('completed.html', requests=requests)
