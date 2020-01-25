from app.api.models import *


class Request(Model):
    id = AutoField()
    category = TextField()
    goods = TextField()
    picture = TextField(default='default.png')
    quantity = IntegerField()
    waiting_period = DateTimeField()
    delivery_date = DateTimeField()
    notes = TextField()

    @staticmethod
    def get_all_categories():
        select_field_options = list()
        select_field_options.append(('1', 'Канцелярия'))
        select_field_options.append(('2', 'Спорт'))
        select_field_options.append(('3', 'Учебники'))
        select_field_options.append(('4', 'Медикаменты'))
        select_field_options.append(('5', 'Инструменты'))
        select_field_options.append(('6', 'Мебель'))
        select_field_options.append(('7', 'Офисные принадлежности'))
        select_field_options.append(('8', 'Продукты питания'))
        select_field_options.append(('9', 'Обувь'))
        return select_field_options

    class Meta:
        database = db
        db_table = 'Requests'
