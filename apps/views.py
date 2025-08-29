from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

from apps.models import Category, FoodImage, Food
from apps.serializers import CategorySerializer, FoodImageSerializer, FoodSerializer


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


@extend_schema(tags=['Food Image'])
class CreateFoodImageApiView(CreateAPIView):
    queryset = FoodImage.objects.all()
    serializer_class = FoodImageSerializer
    parser_classes = [MultiPartParser, FormParser]


@extend_schema(tags=['Food Image'])
class DeleteFoodImageApiView(DestroyAPIView):
    queryset = FoodImage.objects.all()
    serializer_class = FoodImageSerializer


@extend_schema(tags=['Food Image'])
class ListFoodImageApiView(ListAPIView):
    queryset = FoodImage.objects.all()
    serializer_class = FoodImageSerializer


@extend_schema(tags=['Food'])
class CreateFoodApiView(CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser]


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