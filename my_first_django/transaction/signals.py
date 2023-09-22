from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from .models import Transaction


@receiver(post_save, sender=Transaction)
def my_handler(sender, **kwargs):
    Transaction.objects.create(name="Signals!!!")
    print('Transaction is created')
