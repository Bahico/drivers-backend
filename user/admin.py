from django.contrib import admin

from user.models import User


# Register your models here.


@admin.register(User)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'telegram_id', 'chat_id', 'last_name', 'username']
