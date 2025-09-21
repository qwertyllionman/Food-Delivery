from django.db import models
from django.db.models import Model


class Deliver(Model):
    """
    Attributes:
        user (fk) = deliver qaysi userga tegishli ekanligi
        restaurant (fk) = deliver qaysi restaurantga tegishli ekanligi
        status (enum(Preparing, Delivering, Delivered, Canceled)) = deliverning ayni damdagi statusi
        overall (decimal) = Buyurtmaning umumiy summasi
        destination (str) = Qayerga yetkazib berish
    """