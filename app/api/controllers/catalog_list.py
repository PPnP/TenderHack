from flask.views import MethodView
from flask import render_template

from app.api.models.request import Request


class CatalogListController(MethodView):
    def get(self):
        return render_template('catalog_list.html')
