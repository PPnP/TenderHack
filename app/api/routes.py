from flask import Blueprint

api = Blueprint('api', __name__, template_folder='../templates', static_folder='../static')


from app.api.controllers.index import IndexPageController
api.add_url_rule('/', view_func=IndexPageController.as_view('IndexPage'))

from app.api.controllers.catalog import CatalogController
api.add_url_rule('/catalog', view_func=CatalogController.as_view('Catalog'))

from app.api.controllers.create import CreateRequestController
api.add_url_rule('/create', view_func=CreateRequestController.as_view('CreateRequest'))

from app.api.controllers.details import DetailsController
api.add_url_rule('/details/<string:id>', view_func=DetailsController.as_view('Details'))

from app.api.controllers.success import SuccessController
api.add_url_rule('/success', view_func=SuccessController.as_view('Success'))
