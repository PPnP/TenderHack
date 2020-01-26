from flask.views import MethodView
from flask import render_template


class SupplierController(MethodView):
    def get(self):
        customers = [
            {
                'id': '1',
                'name': 'НИУ ВШЭ',
                'address': 'Кременчугская, 5/3',
                'lat': '55.722390',
                'long': '37.464221'
            },
            {
                'id': '2',
                'name': 'ЛИТ 1533',
                'address': 'Ломоносовский, 16',
                'lat': '55.692338',
                'long': '37.543731'
            },
            {
                'id': '3',
                'name': 'ЛИТ 1533 Библиотека',
                'address': 'Ломоносовский, 18',
                'lat': '55.691826',
                'long': '37.540784'
            },
            {
                'id': '4',
                'name': 'ДИТ г. Москвы',
                'address': 'Новая Басманная ул., 10 стр.1',
                'lat': '55.768983',
                'long': '37.656335'
            },
            {
                'id': '5',
                'name': 'ООО ППнП Тех',
                'address': 'Красная площадь, 3',
                'lat': '55.754638',
                'long': '37.621633'
            }
        ]
        return render_template('supplier.html', customers=customers)
