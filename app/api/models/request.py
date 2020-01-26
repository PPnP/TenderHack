from app.api.models import *


class Request(Model):
    id = AutoField()
    category = TextField()
    goods = TextField()
    picture = TextField(default='default.png')
    quantity = IntegerField()
    waiting_period = DateTimeField()
    delivery_date = DateTimeField()
    notes = TextField(null=True, default='')
    is_completed = BooleanField(default=False)

    @staticmethod
    def get_all_categories():
        select_field_options = list()
        select_field_options.append(('Канцелярия', 'Канцелярия'))
        select_field_options.append(('Спорт', 'Спорт'))
        select_field_options.append(('Учебники', 'Учебники'))
        select_field_options.append(('Медикаменты', 'Медикаменты'))
        select_field_options.append(('Инструменты', 'Инструменты'))
        select_field_options.append(('Мебель', 'Мебель'))
        select_field_options.append(('Офисные принадлежности', 'Офисные принадлежности'))
        select_field_options.append(('Продукты питания', 'Продукты питания'))
        select_field_options.append(('Обувь', 'Обувь'))
        select_field_options.append(('Бытовая техника', 'Бытовая техника'))
        select_field_options.append(('Развлечения', 'Развлечения'))
        return select_field_options

    class Meta:
        database = db
        db_table = 'Requests'
