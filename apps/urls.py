"""
URL configuration for FoodDelivery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from apps.views import CreateCategoryApiView, DeleteCategoryApiView, ListCategoryApiView, CreateFoodImageApiView, \
    DeleteFoodImageApiView, ListFoodImageApiView, DeleteFoodApiView, UpdateFoodApiView, ListFoodApiView, \
    RetrieveFoodApiView, CreateFoodApiView

urlpatterns = []

# ---------------------------------- Category ----------------------------------------------
urlpatterns += [
    path('api/v1/category/create', CreateCategoryApiView.as_view()),
    path('api/v1/category/list', ListCategoryApiView.as_view()),

    path('api/v1/category/<int:pk>', DeleteCategoryApiView.as_view()),

]

# ---------------------------------- Food Image -------------------------------------------
urlpatterns += [
    path('api/v1/food-image/create', CreateFoodImageApiView.as_view()),
    path('api/v1/food-image/<int:pk>', DeleteFoodImageApiView.as_view()),
    path('api/v1/food-image/list', ListFoodImageApiView.as_view()),
]
# ----------------------------------- Food --------------------------------------------------
urlpatterns += [
    path('api/v1/food/create', CreateFoodApiView.as_view()),
    path('api/v1/food/<int:pk>/delete', DeleteFoodApiView.as_view()),
    path('api/v1/food/<int:pk>/update', UpdateFoodApiView.as_view()),
    path('api/v1/food/list', ListFoodApiView.as_view()),
    path('api/v1/food/<int:pk>/get', RetrieveFoodApiView.as_view())
]
