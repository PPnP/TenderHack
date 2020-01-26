from flask.views import MethodView
from flask import redirect


class DefaultIndexController(MethodView):
    def get(self):
        return redirect('/1')
