from app.api.models import *


class Customer(Model):
    id = AutoField()
    name = TextField(default='Arkasha')
    region = TextField()
    address = TextField()

    class Meta:
        database = db
        db_table = 'Customers'
