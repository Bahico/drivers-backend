from django.db import models

from user.models import User


# Create your models here.

class DriverOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='queue')
    order = models.IntegerField(default=0)


class Message(models.Model):
    message_id = models.IntegerField(unique=True)
    text = models.TextField(blank=True, null=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    drivers = models.ManyToManyField(DriverOrder, default=[], related_name='queue_message')
    driver_order_index = models.IntegerField(default=0)
    accept_driver = models.ForeignKey(DriverOrder, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text


class SendMessage(models.Model):
    chat_id = models.CharField(max_length=255)
    client_message_id = models.IntegerField()
    message_id = models.IntegerField()
    voice = models.BooleanField(default=False)
