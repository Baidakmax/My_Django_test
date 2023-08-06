from django.contrib import admin
from .models import Category, Good, Tag


# Register your models here.
class GoodAdmin(admin.ModelAdmin):

    list_display = ['id', 'name','active', 'price', 'country', 'category']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'id']
    list_filter = ['price', 'active', 'category']


class GoodsAdminInLine(admin.StackedInline):
    model = Good.tags.through
    extra = 2


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'uuid']
    inlines = [GoodsAdminInLine]


admin.site.register(Category)
admin.site.register(Good, GoodAdmin)
admin.site.register(Tag, TagAdmin)