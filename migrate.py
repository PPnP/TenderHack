from app.api.models.request import Request
from app.api.models.customer import Customer
from app.api.models.customer_to_request import CustomerRequest

import datetime

Request.drop_table()
Request.create_table()

Customer.drop_table()
Customer.create_table()

CustomerRequest.drop_table()
CustomerRequest.create_table()

r1 = Request.create(category='Канцелярия', goods='Степлер', picture='stepler.jpg', quantity=10,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=5),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=8), notes='')
r2 = Request.create(category='Офисные принадлежности', goods='Бумага SvetoCopy', picture='svetocopy.jpg', quantity=7,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=4),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=20), notes='')
r3 = Request.create(category='Быт', goods='Кофемашина', picture='coffee.jpg', quantity=1,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=3),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=7), notes='')
r4 = Request.create(category='Обувь', goods='Yeezy Boost', picture='yeezy.webp', quantity=2,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=2),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=5), notes='', is_completed=True)
r5 = Request.create(category='Бытовая техника', goods='Шуруповёрт', picture='screwdriver.jpg', quantity=4,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=3),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=7), notes='', is_completed=True)
r6 = Request.create(category='Развлечения', goods='Кубик Рубика', picture='cube.jpg', quantity=4,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=5),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=7), notes='')

c1 = Customer.create(name='Stepan Denisov', location='15-я Парковая, 16к3')
c2 = Customer.create(name='Pavel Krylov', location='Широкая, 8')
c3 = Customer.create(name='Leonid Kravtsov', location='Первомайская, 121')
c4 = Customer.create(name='Matvey Kottsov', location='Покровский бульвар, 11')
c5 = Customer.create(name='Ivan Ivanov', location='Академика Скрябина, 26к1')
c6 = Customer.create(name='Petr Parker', location='Большая грузинская, 12с2')

CustomerRequest.create(customer=c1, request=r1)
CustomerRequest.create(customer=c2, request=r2)
CustomerRequest.create(customer=c3, request=r3)
CustomerRequest.create(customer=c4, request=r4)
CustomerRequest.create(customer=c5, request=r5)
CustomerRequest.create(customer=c6, request=r6)
