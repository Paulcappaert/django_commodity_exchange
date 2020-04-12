from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CommodityListView.as_view(), name='commodities'),
    path('api/<str:pk>', views.CommodityDetail.as_view(), name='api-commodity-detail'),
    path('api', views.CommoditiesList.as_view(), name='api-commidities'),
]