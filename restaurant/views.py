from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer

@extend_schema(tags=['Restaurant'])
class CreateRestaurantAPIView(CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

@extend_schema(tags=['Restaurant'])
class GetRestaurantListApiView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

@extend_schema(tags=['Restaurant'])
class GetRestaurantApiView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

@extend_schema(tags=['Restaurant'])
class UpdateRestaurantApiView(UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

@extend_schema(tags=['Restaurant'])
class DeleteRestaurantApiView(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

