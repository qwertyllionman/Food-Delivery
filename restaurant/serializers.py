from rest_framework.serializers import ModelSerializer

from food.serializers import FoodSerializer
from restaurant.models import Restaurant


class RestaurantSerializer(ModelSerializer):
    foods = FoodSerializer(read_only=True, many=True)
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone_number', 'working_time', 'delivery_fee', 'foods']
