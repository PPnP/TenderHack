from flask import Blueprint

api = Blueprint('api', __name__, template_folder='../templates', static_folder='../static')


from app.api.controllers.index import IndexPageController
api.add_url_rule('/', view_func=IndexPageController.as_view('IndexPage'))

from app.api.controllers.catalog import CatalogController
api.add_url_rule('/catalog', view_func=CatalogController.as_view('Catalog'))
