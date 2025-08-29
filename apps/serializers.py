from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Food, FoodImage


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'id']
        read_only_fields = ['id']

    def validate_name(self, value):
        if Category.objects.filter(name=value).first():
            raise ValidationError("This category is already exists!")
        return value


class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"
        read_only_fields = ['id']


class FoodImageSerializer(ModelSerializer):
    class Meta:
        model = FoodImage
        fields = "__all__"
        read_only_fields = ['id']
