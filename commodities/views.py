from .models import Commodity
from .serializers import CommoditySerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.views.generic import ListView

class CommodityListView(ListView):
    model = Commodity
    template_name = 'commodities/commodities.html'
    context_object_name = 'commodities'

class CommoditiesList(generics.ListCreateAPIView):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
    permission_classes = (IsAuthenticated,)

class CommodityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
    permission_classes = (IsAuthenticated,)