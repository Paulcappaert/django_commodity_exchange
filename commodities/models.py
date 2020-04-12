from django.db import models
from core.models import User

class Commodity(models.Model):
    symbol = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=100)

    def price(self):
        if self.trade_set.exists():
            price = self.trade_set.all().order_by('ts').last().price
            return str(price * .01)
        return 'null'

class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    quant = models.IntegerField()

class Trade(models.Model):
    ts = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='sales'
    )
    buyer = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='purchases'
    )
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    quant = models.IntegerField()
    price = models.IntegerField()
