from rest_framework import serializers
from .models import Commodity, Trade

class CommoditySerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Commodity
        fields = '__all__'

    def get_price(self, instance):
        if Trade.objects.filter(commodity=instance).exists():
            return Trade.objects.filter(commodity=instance).order_by('-price').first().price
        else:
            return None