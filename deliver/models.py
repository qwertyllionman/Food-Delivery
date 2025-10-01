from django.db import models
from django.db.models import Model, ForeignKey, CASCADE, SET_NULL, CharField, TextChoices, DecimalField


class Deliver(Model):
    class Status(TextChoices):
        PREPARING = "preparing", "Preparing"
        DELIVERING = "delivering", "Delivering"
        DELIVERED = "delivered", "Delivered"
        CANCELED = "canceled", "Canceled"

    user = ForeignKey("account.User", on_delete=CASCADE, related_name="delivers")
    restaurant = ForeignKey("restaurant.Restaurant", on_delete=CASCADE, related_name="delivers")
    deliver_detail = ForeignKey("deliver.DeliverDetail", on_delete=CASCADE, related_name="delivers")
    status = CharField(max_length=255, choices=Status, default=Status.PREPARING)
    overall = DecimalField(max_digits=10, decimal_places=2, default=0)
    destination = CharField(max_length=255)


    """
    Attributes:
        user (fk) = deliver qaysi userga tegishli ekanligi
        restaurant (fk) = deliver qaysi restaurantga tegishli ekanligi
        deliver (fk) = deliverdagi mahsulotlar
        status (enum(Preparing, Delivering, Delivered, Canceled)) = deliverning ayni damdagi statusi
        overall (decimal) = Buyurtmaning umumiy summasi
        destination (str) = Qayerga yetkazib berish
    """

class DeliverDetail(Model):
    deliver = ForeignKey("deliver.Deliver", on_delete=SET_NULL, related_name="deliver_details", blank=True, null=True)
    food = ForeignKey("food.Food", on_delete=CASCADE, related_name="deliver_details")
    """
    This is for many to many
    Attributes:
        deliver (fk) = Deliverga bog'lash
        food (fk) = Foodga bog'lash
    """