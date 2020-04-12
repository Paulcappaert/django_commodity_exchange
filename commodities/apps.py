from django.apps import AppConfig


class CommoditiesConfig(AppConfig):
    name = 'commodities'

    def ready(self):
        import commodities.signals
