from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import filters
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

from food.models import Category, Food, Bonus
from food.serializers import CategorySerializer, FoodSerializer, BonusSerializer


@extend_schema(tags=['Category'])
class CreateCategoryApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser]


@extend_schema(tags=['Category'])
class DeleteCategoryApiView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=['Category'])
class ListCategoryApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@extend_schema(tags=['Category'])
class GetCategoryApiView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# @extend_schema(tags=['Food Image'])
# class CreateFoodImageApiView(CreateAPIView):
#     queryset = FoodImage.objects.all()
#     serializer_class = FoodImageSerializer
#     parser_classes = [MultiPartParser, FormParser]


# @extend_schema(tags=['Food Image'])
# class DeleteFoodImageApiView(DestroyAPIView):
#     queryset = FoodImage.objects.all()
#     serializer_class = FoodImageSerializer


# @extend_schema(tags=['Food Image'])
# class ListFoodImageApiView(ListAPIView):
#     queryset = FoodImage.objects.all()
#     serializer_class = FoodImageSerializer


@extend_schema(tags=['Food'])
class CreateFoodApiView(CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser]

    def perform_create(self, serializer):
        bonus_price = float(serializer.validated_data["bonus_price"])
        price = float(serializer.validated_data["price"])
        if price >= bonus_price:
            price -= bonus_price
        serializer.save(price=price)

@extend_schema(tags=['Food'])
class UpdateFoodApiView(UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


@extend_schema(tags=['Food'])
class DeleteFoodApiView(DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


@extend_schema(tags=['Food'])
class ListFoodApiView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

@extend_schema(tags=['Food'])
class RetrieveFoodApiView(RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

@extend_schema(tags=['Bonus'])
class CreateBonusApiView(CreateAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

@extend_schema(tags=['Bonus'])
class ListBonusApiView(ListAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

@extend_schema(tags=['Bonus'])
class GetBonusApiView(RetrieveAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

@extend_schema(tags=['Bonus'])
class UpdateBonusApiView(UpdateAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

@extend_schema(tags=['Bonus'])
class DeleteBonusApiView(DestroyAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

@extend_schema(tags=['Filtering and Searching'])
class SearchFoodAPIView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name'] # TODO for restaurant filter

