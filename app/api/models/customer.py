from app.api.models import *


class Customer(Model):
    id = AutoField()
    name = TextField(default='Arkasha')
    location = TextField()

    class Meta:
        database = db
        db_table = 'Customers'
