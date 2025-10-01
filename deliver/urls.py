from django.urls import path

from deliver.views import CreateDeliverDetailAPIView, ListDeliverDetailAPIView, RetrieveDeliverAPIView, \
    RetrieveDeliverDetailAPIView, UpdateDeliverDetailAPIView, DeleteDeliverDetailAPIView, CreateDeliverAPIView, \
    ListDeliverAPIView, UpdateDeliverAPIView, DeleteDeliverAPIView

# -------------------------------------------- Deliver Detail -----------------------------------
urlpatterns = [
    path('api/v1/delivery-detail/create', CreateDeliverDetailAPIView.as_view()),
    path('api/v1/delivery-detail/list', ListDeliverDetailAPIView.as_view()),
    path('api/v1/delivery-detail/<int:pk>', RetrieveDeliverDetailAPIView.as_view()),
    path('api/v1/delivery-detail/<int:pk>', UpdateDeliverDetailAPIView.as_view()),
    path('api/v1/delivery-detail/<int:pk>', DeleteDeliverDetailAPIView.as_view()),

]

# ------------------------------------------- Deliver --------------------------------------------
urlpatterns += [
    path('api/v1/deliver/create', CreateDeliverAPIView.as_view()),
    path('api/v1/deliver/list', ListDeliverAPIView.as_view()),
    path('api/v1/deliver/<int:pk>', RetrieveDeliverAPIView.as_view()),
    path('api/v1/deliver/update/<int:pk>', UpdateDeliverAPIView.as_view(), name="update"),
    path('api/v1/deliver/<int:pk>', DeleteDeliverAPIView.as_view()),
]