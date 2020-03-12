from django.contrib import admin
from .models import Commodity, Balance, Trade

admin.site.register(Commodity)
admin.site.register(Balance)
admin.site.register(Trade)
