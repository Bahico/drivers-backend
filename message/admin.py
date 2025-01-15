from django.contrib import admin

from message.models import Message, DriverOrder, SendMessage


# Register your models here.


@admin.register(Message)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'message_id', 'text', 'client', 'driver_order_index', 'accept_driver_id']


@admin.register(DriverOrder)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order']


@admin.register(SendMessage)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'client_message_id', 'message_id', 'voice']
