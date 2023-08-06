from django.core.management.base import BaseCommand
from crypto_currency.models import BTC
from crypto_currency.crypto_binance_api import currency_crypto




dict_of_coins = currency_crypto()
print(dict_of_coins)

class Command(BaseCommand):
    help_text = 'fill db to BTC'


    def handle(self, *args, **options):
        for key, value in dict_of_coins.items():
            time_zone = value[1]
            BTC.objects.create(name=key, price=value[0])

    print("BTC is created")