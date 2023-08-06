from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class BTC(models.Model):
    name = models.CharField("name", max_length=40)
    price = models.FloatField('Currency', default=0)
    time_crypto = models.CharField(max_length=40, default="time")
    # time_price = RichTextField(default="time")

    class Meta:
        verbose_name = 'Coin'
        verbose_name_plural = 'Crypto_currency'
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}, ціна: {self.price}"
