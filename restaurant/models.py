from django.db.models import Model, CharField, DecimalField


class Restaurant(Model):
    name = CharField(max_length=255)
    address = CharField(max_length=255)
    phone_number = CharField(max_length=15)
    working_time = CharField(max_length=50)
    delivery_fee = DecimalField(max_digits=10, decimal_places=2)
