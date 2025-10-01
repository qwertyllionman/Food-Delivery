from rest_framework.serializers import ModelSerializer

from deliver.models import Deliver, DeliverDetail


class DeliverSerializer(ModelSerializer):
    class Meta:
        model = Deliver
        fields = ["id", "restaurant", "user", "deliver_detail", "status", "overall", "destination"]


class DeliverDetailSerializer(ModelSerializer):
    class Meta:
        model = DeliverDetail
        fields = ["id", "deliver", "food"]