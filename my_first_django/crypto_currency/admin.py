from django.contrib import admin
from .models import BTC

# Register your models here.



class BtcAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.register(BTC, BtcAdmin)