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

r1 = Request.create(category='Канцелярия', goods='Степлер', picture='stepler1.jpg', quantity=10,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=5),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=8))
r2 = Request.create(category='Офисные принадлежности', goods='Бумага SvetoCopy', picture='svetocopy.jpg', quantity=7,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=4),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=20))
r3 = Request.create(category='Бытовая техника', goods='Кофемашина', picture='coffee.jpg', quantity=1,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=3),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=7))
r4 = Request.create(category='Обувь', goods='Yeezy Boost', picture='yeezy.webp', quantity=2,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=2),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=5))
r5 = Request.create(category='Бытовая техника', goods='Шуруповёрт', picture='screwdriver.jpg', quantity=4,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=3),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=7))
r6 = Request.create(category='Развлечения', goods='Кубик Рубика', picture='cube.jpg', quantity=4,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=5),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=7))
r7 = Request.create(category='Офисные принадлежности', goods='Принтер', quantity=4,
                    waiting_period=datetime.date.today() - datetime.timedelta(days=5),
                    delivery_date=datetime.date.today() - datetime.timedelta(days=3), is_completed=True)
r8 = Request.create(category='Бытовая техника', goods='Мультиварка', quantity=9,
                    waiting_period=datetime.date.today() - datetime.timedelta(days=3),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=7), is_completed=True)
r9 = Request.create(category='Канцелярия', goods='Степлер', picture='stepler2.jpg', quantity=9,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=4),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=9))
r10 = Request.create(category='Канцелярия', goods='Степлер', picture='stepler3.jpeg', quantity=6,
                    waiting_period=datetime.date.today() + datetime.timedelta(days=2),
                    delivery_date=datetime.date.today() + datetime.timedelta(days=5))

c1 = Customer.create(name='Stepan Denisov', region='Moscow', address='15-я Парковая, 16к3')
c2 = Customer.create(name='Pavel Krylov', region='Moscow', address='Широкая, 8')
c3 = Customer.create(name='Leonid Kravtsov', region='Moscow', address='Первомайская, 121')
c4 = Customer.create(name='Matvey Kottsov', region='Moscow', address='Покровский бульвар, 11')
c5 = Customer.create(name='Ivan Ivanov', region='Moscow', address='Академика Скрябина, 26к1')
c6 = Customer.create(name='Petr Parker', region='Moscow', address='Большая Грузинская, 12с2')
c7 = Customer.create(name='John the Baptist', region='Moscow', address='Маршала Жукова, 28')
c8 = Customer.create(name='Alex Ovechkin', region='Moscow', address='Мякининская, 46')
c9 = Customer.create(name='Lol Kek', region='Moscow', address='Мякининская, 46')
c10 = Customer.create(name='Ilon Mask', region='Moscow', address='Мякининская, 46')

CustomerRequest.create(customer=c1, request=r1)
CustomerRequest.create(customer=c2, request=r2)
CustomerRequest.create(customer=c3, request=r3)
CustomerRequest.create(customer=c4, request=r4)
CustomerRequest.create(customer=c5, request=r5)
CustomerRequest.create(customer=c6, request=r6)
CustomerRequest.create(customer=c7, request=r7)
CustomerRequest.create(customer=c8, request=r8)
CustomerRequest.create(customer=c9, request=r9)
CustomerRequest.create(customer=c10, request=r10)
