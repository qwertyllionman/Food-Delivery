from django.db.models import Model, CharField, ForeignKey, CASCADE, DecimalField, BooleanField, TextField, ImageField, \
    SET_NULL, IntegerField


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Food(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=9, decimal_places=2)
    category = ForeignKey("food.Category", on_delete=SET_NULL, related_name='foods', null=True, blank=True)
    is_available = BooleanField(default=False)
    image_url = TextField(null=True, blank=True)
    description = TextField(null=True, blank=True)
    bonus_price = DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    rate = DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    overall = DecimalField(max_digits=9, decimal_places=2)
    bonus_section = ForeignKey("food.Bonus", on_delete=SET_NULL, related_name='foods', null=True, blank=True)
    restaurant = ForeignKey("restaurant.Restaurant", on_delete=CASCADE, related_name="foods", null=True, blank=True)

    def __str__(self):
        return self.name


class Bonus(Model):
    buy_count = IntegerField(default=1)
    add = IntegerField(default=0)
    banner_image_url = TextField(null=True, blank=True)

# class FoodImage(Model):
#     photo = ImageField(upload_to='foods/')
#     food = ForeignKey('food.Food', on_delete=SET_NULL, related_name='food_images', null=True, blank=True)
