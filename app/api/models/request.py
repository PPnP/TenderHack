from app.api.models import *


class Request(Model):
    id = AutoField()
    category = TextField()
    goods = TextField()
    picture = TextField(default='default.png')
    quantity = IntegerField()
    waiting_period = DateTimeField()
    delivery_date = DateTimeField()

    class Meta:
        database = db
        db_table = 'Requests'
