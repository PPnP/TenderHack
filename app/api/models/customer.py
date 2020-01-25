from app.api.models import *


class Customer(Model):
    id = AutoField()
    name = TextField(null=True, default=None)
    location = TextField()

    class Meta:
        database = db
        db_table = 'Customers'
