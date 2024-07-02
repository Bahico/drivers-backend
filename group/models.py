from django.db import models


# Create your models here.

class GroupType(models.IntegerChoices):
    GET_MESSAGE = 1
    SEND_MESSAGE = 2


class Group(models.Model):
    name = models.CharField(max_length=255)
    telegram_id = models.IntegerField()
    type = models.IntegerField(choices=GroupType)
