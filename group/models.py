from django.db import models

# Create your models here.

groupType = (
    (1, 'GET_MESSAGE'),
    (2, 'SEND_MESSAGE')
)


class Group(models.Model):
    name = models.CharField(max_length=255)
    telegram_id = models.CharField(max_length=255)
    type = models.IntegerField(choices=groupType)
