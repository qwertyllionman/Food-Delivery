from django.db.models import Model, CharField, ForeignKey, CASCADE, DecimalField, BooleanField, TextField, ImageField, \
    SET_NULL, IntegerField


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Food(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=9, decimal_places=2)
    category = ForeignKey("apps.Category", on_delete=SET_NULL, related_name='foods', null=True, blank=True)
    is_available = BooleanField(default=False)
    description = TextField(null=True, blank=True)
    bonus_price = DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    rate = DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    first_section = IntegerField(default=1)
    second_section = IntegerField(default=0)

    def __str__(self):
        return self.name


class FoodImage(Model):
    photo = ImageField(upload_to='foods/')
    food = ForeignKey('apps.Food', on_delete=SET_NULL, related_name='food_images', null=True, blank=True)
