from django.db import models
from core.models import User
from commodities.models import Commodity

class Offer(models.Model):
    TYPES = (
        ('b', 'Buy'),
        ('s', 'Sell'),
    )

    type = models.CharField(max_length=1, choices=TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    price = models.IntegerField()
    quant = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def exchange(self, _party, _price, _quant):
        pass
