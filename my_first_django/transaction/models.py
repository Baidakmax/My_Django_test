from django.db import models

class Transaction(models.Model):
    name = models.CharField('Name', max_length=20, blank=True, unique=True)
    price = models.FloatField("Price", default=0.0)
    active = models.BooleanField("Active", default=False)
    create = models.DateTimeField("Crate", auto_now_add=True, null=True, editable=True)
    update = models.DateTimeField("Update" , auto_now_add=True, null=True, editable=True)

    class Meta:
        verbose_name = 'Транзакції'
        verbose_name_plural = 'Транзакції'
        ordering = ('id',)

    def __str__(self):
        return self.name

