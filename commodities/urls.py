from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CommoditiesList.as_view(), name='commidities'),
]