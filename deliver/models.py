from django.db import models
from django.db.models import Model


class Deliver(Model):
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
    """
    This is for many to many
    Attributes:
        deliver (fk) = Deliverga bog'lash
        food (fk) = Foodga bog'lash
    """