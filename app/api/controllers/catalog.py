from flask.views import MethodView
from flask import render_template

from app.api.models.request import Request


class CatalogController(MethodView):
    def get(self):
        requests = Request.select()
        return render_template('catalog.html', requests=requests, categories=Request.get_all_categories())
