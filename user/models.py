from django.db import models


# Create your models here.

class UserType(models.IntegerChoices):
    ADMIN = 1
    DRIVER = 2
    SIMPLE = 3


class User(models.Model):
    telegram_id = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(choices=UserType, default=UserType.SIMPLE)


class UserStage(models.Model):
    telegram_id = models.CharField(max_length=200, unique=True)
    step = models.CharField(max_length=200)
    step_under = models.CharField(max_length=200, blank=True, null=True)
