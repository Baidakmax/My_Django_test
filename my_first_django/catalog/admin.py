from django.contrib import admin
from .models import Category, Good


# Register your models here.
class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','active', 'price', 'country']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'id']
    list_filter = ['price', 'active']






admin.site.register(Category)
admin.site.register(Good, GoodAdmin)