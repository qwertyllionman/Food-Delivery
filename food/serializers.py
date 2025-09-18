from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from food.models import Category, Food, Bonus


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'id']

    def validate_name(self, value):
        if Category.objects.filter(name=value).first():
            raise ValidationError("This category is already exists!")
        return value


class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = ["id", "name", "price", "category", "is_available", "image_url", "description", "bonus_price", "rate",
                  "bonus_section", "restaurant"]


class BonusSerializer(ModelSerializer):
    class Meta:
        model = Bonus
        fields = ["id", 'buy_count','add']

# class FoodImageSerializer(ModelSerializer):
#     class Meta:
#         model = FoodImage
#         fields = "__all__"
