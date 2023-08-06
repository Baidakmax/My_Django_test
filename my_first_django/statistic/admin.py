from django.contrib import admin
from .models import UserStat


class UserStatAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_at', 'headers']


admin.site.register(UserStat, UserStatAdmin)