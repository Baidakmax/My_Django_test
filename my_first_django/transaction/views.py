from django.shortcuts import render
from .models import Transaction
from django.db import transaction
# Create your views here.

def first():
    Transaction.objects.create(name="Списання")



def second():
    Transaction.objects.create(name='Зачислення')

@transaction.atomic
def start():
    first()
    second()