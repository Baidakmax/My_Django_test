import requests
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

URL = 'https://playfootball.com.ua'

class Command(BaseCommand):

    def handle(self, *args, **options):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) '
                          'Gecko / 20100101 Firefox / 71.0', 'accept': ' * / * '
        }
        r = requests.get(URL, headers)
        bs = BeautifulSoup(r.content, 'html5lib')
        for item in bs.findAll("a", {'class': "main-nav__link"}):
            # print(item['href'])
            good_url = item['href']
            rq = requests.get(good_url, headers)
            bs_good = BeautifulSoup(rq.content, 'html5lib')
            goods = bs_good.findAll('div', {'class': "col-xs-12 col-sm-6 col-md-4 col-lg-4"})
            for item_goods in goods:
                good_name = item_goods.select_one('.product-cut__title').get_text()
                print(good_name)
                godd_price = item_goods.select_one(".product-cut__price").get_text()
                print(godd_price)



