from django.db import models
from rest_framework.pagination import PageNumberPagination

# Create your models here.

userType = (
    (1, 'ADMIN'),
    (2, 'DRIVER'),
    (3, 'SIMPLE'),
)


class User(models.Model):
    telegram_id = models.CharField(max_length=200, unique=True)
    chat_id = models.CharField(max_length=200, unique=True, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(choices=userType, default=3)


class UserStage(models.Model):
    telegram_id = models.CharField(max_length=200, unique=True)
    step = models.CharField(max_length=200)
    step_under = models.CharField(max_length=200, blank=True, null=True)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ActivationKey(models.Model):
    activation_key = models.CharField(max_length=150)
