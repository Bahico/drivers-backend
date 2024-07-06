from django.db import models


# Create your models here.

userType = (
    (1, 'ADMIN'),
    (2, 'DRIVER'),
    (3, 'SIMPLE'),
)


class User(models.Model):
    telegram_id = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(choices=userType, default=3)


class UserStage(models.Model):
    telegram_id = models.CharField(max_length=200, unique=True)
    step = models.CharField(max_length=200)
    step_under = models.CharField(max_length=200, blank=True, null=True)
