from django.contrib import admin
from .models import Category, Good, Tag
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class GoodAdmin(admin.ModelAdmin):

    list_display = ['id', 'name','active','image_thumbnail', 'price', 'country', 'category']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'id']
    list_filter = ['price', 'active', 'category']


class GoodsAdminInLine(admin.StackedInline):
    model = Good.tags.through
    extra = 2


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'uuid']
    inlines = [GoodsAdminInLine]


admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Tag, TagAdmin)