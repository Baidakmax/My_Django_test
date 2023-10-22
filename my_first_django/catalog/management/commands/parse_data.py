import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from catalog.models import Category, Good
from bs4 import BeautifulSoup

URL = 'https://ukrzoloto.ua'


class Command(BaseCommand):

    @staticmethod
    def download_image(image_url, image_name):
        imagename = f'{settings.BASE_DIR}/media/image/{image_name}.jpg'

        img_data = requests.get(image_url).content
        with open(imagename, 'wb') as handler:
            handler.write(img_data)

        return imagename

    def handle(self, *args, **options):
        r = requests.get(URL + '/catalog')
        bs = BeautifulSoup(r.content, 'html5lib')
        for item in bs.findAll("a", {'class': 'catalogue-categories__link'}):
            cat = Category.objects.get_or_create(name=item.get_text(), description=item.get_text())
            good_url = URL + item['href']
            rq = requests.get(good_url)
            bs_good = BeautifulSoup(rq.content, 'html5lib')
            goods = bs_good.findAll('div', {'class': 'product-card'})
            for index, good_item in enumerate(goods):
                good_name = good_item.select_one('.title').get_text()
                # print(good_name)
                good_image = good_item.select_one("img")['src']
                # print(good_image)
                good_price = good_item.select_one('.price__current span').get_text()
                # print(good_price)
                Good.objects.get_or_create(
                    name= good_name,
                    description=good_name,
                    price= float(good_price.replace(' ', '')),
                    active=True,
                    category=cat[0],
                    image= self.download_image(good_image, index)
                )