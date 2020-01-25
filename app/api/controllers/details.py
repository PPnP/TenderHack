from flask.views import MethodView
from flask import render_template

from app.api.models.request import Request


class DetailsController(MethodView):
    def get(self, id):
        request = Request.get(Request.id == id)
        return render_template('details.html', request=request, id=id)
