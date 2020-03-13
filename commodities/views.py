from .models import Commodity
from .serializers import CommoditySerializer
from rest_framework import generics


class CommoditiesList(generics.ListCreateAPIView):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer

class CommodityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer