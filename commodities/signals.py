from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Commodity, Trade

@receiver(post_save, sender=Trade)
def update_price(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "all", 
            {
            "type": "price_update",
            'message': {
                'symbol': instance.commodity.symbol,
                'price': instance.price * .01,
                }
            }
        )
