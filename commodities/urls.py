from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:pk>', views.CommodityDetail.as_view(), name='commodity-detail'),
    path('', views.CommoditiesList.as_view(), name='commidities'),
]