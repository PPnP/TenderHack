from app.api.models import *

from app.api.models.customer import Customer
from app.api.models.request import Request


class CustomerRequest(Model):
    customer = ForeignKeyField(Customer)
    request = ForeignKeyField(Request)

    class Meta:
        database = db
        db_table = 'CustomerRequests'
