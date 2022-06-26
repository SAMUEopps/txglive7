from django.apps import AppConfig


class CashbagConfig(AppConfig):
    name = 'cashbag'

    def ready(self):
    	import cashbag.signals
