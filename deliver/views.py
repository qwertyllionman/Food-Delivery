from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from deliver.models import DeliverDetail, Deliver
from deliver.serializers import DeliverDetailSerializer, DeliverSerializer


# Create your views here.
@extend_schema(tags=['Deliver Detail'])
class CreateDeliverDetailAPIView(CreateAPIView):
    queryset = DeliverDetail.objects.all()
    serializer_class = DeliverDetailSerializer

@extend_schema(tags=['Deliver Detail'])
class RetrieveDeliverDetailAPIView(RetrieveAPIView):
    queryset = DeliverDetail.objects.all()
    serializer_class = DeliverDetailSerializer

@extend_schema(tags=['Deliver Detail'])
class ListDeliverDetailAPIView(ListAPIView):
    queryset = DeliverDetail.objects.all()
    serializer_class = DeliverDetailSerializer

@extend_schema(tags=['Deliver Detail'])
class UpdateDeliverDetailAPIView(UpdateAPIView):
    queryset = DeliverDetail.objects.all()
    serializer_class = DeliverDetailSerializer

@extend_schema(tags=['Deliver Detail'])
class DeleteDeliverDetailAPIView(DestroyAPIView):
    queryset = DeliverDetail.objects.all()
    serializer_class = DeliverDetailSerializer

@extend_schema(tags=['Deliver'])
class CreateDeliverAPIView(CreateAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer

    def perform_create(self, serializer):
        deliver = serializer.save()
        deliver_details = DeliverDetail.objects.filter(pk=deliver.id)
        overall= 0
        for detail in deliver_details:
            overall += detail.food.price
        serializer.save(overall=overall)

    # def perform_create(self, serializer):
    #     bonus_price = float(serializer.validated_data["bonus_price"])
    #     price = float(serializer.validated_data["price"])
    #     if price >= bonus_price:
    #         price -= bonus_price
    #     serializer.save(price=price)
@extend_schema(tags=['Deliver'])
class ListDeliverAPIView(ListAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer

@extend_schema(tags=['Deliver'])
class RetrieveDeliverAPIView(RetrieveAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer

@extend_schema(tags=['Deliver'])
class UpdateDeliverAPIView(UpdateAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer

@extend_schema(tags=['Deliver'])
class DeleteDeliverAPIView(DestroyAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer

"""
Delivery uchun CRUD operatsiyalari bo'ladi
Create:
    Delivery yaratilganda overall price avtomatik hisoblanadi restarantni delivery_fee si qo'shiladi
    Many to many bo'lib bog'lanadi Delivery Detail ga (qaysi food qaysi deliveryga tegishli ekanligi) 
    
GET:
    barcha deliverylar olinadi (listda) (User olinganda unga tegishli deliverylarni ham chiqarish mumkin)
    Ma'lum bir delivery ham id bo'yicha olinadi
    
PUT/PATCH:
    Delivery statusi o'zgarib turadi (Preparing, Delivering, Delivered, Canceled)

Ushbu joyda DELETE methodi bo'lishi mumkin edi lekin DELETE o'rniga historyga qo'shiladi DELIVERED
yoki CANCELED statusli deliverylar 
"""
