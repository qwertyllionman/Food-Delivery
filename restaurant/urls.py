from django.urls import path

from restaurant.views import CreateRestaurantAPIView, GetRestaurantListApiView, GetRestaurantApiView, \
    UpdateRestaurantApiView, DeleteRestaurantApiView

urlpatterns = [
    path("api/v1/restaurant/create", CreateRestaurantAPIView.as_view()),
    path("api/v1/restaurant/list", GetRestaurantListApiView.as_view()),
    path("api/v1/restaurant/get/<int:pk>", GetRestaurantApiView.as_view()),
    path("api/v1/restaurant/update/<int:pk>", UpdateRestaurantApiView.as_view()),
    path("api/v1/restaurant/delete/<int:pk>", DeleteRestaurantApiView.as_view()),

]