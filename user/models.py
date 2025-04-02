from django.db import models
from rest_framework.pagination import PageNumberPagination
from django.contrib.postgres.fields import ArrayField
from enum import Enum

# Create your models here.


class UserRole(Enum):
    ADMIN = 'admin'
    DRIVER = 'driver'
    SIMPLE = 'simple'

    @classmethod
    def choices(cls):
        return [(key, key.value) for key in cls]


class User(models.Model):
    telegram_id = models.TextField(max_length=200)
    chat_id = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    roles = ArrayField(
        models.IntegerField(choices=UserRole.choices(), default=UserRole.SIMPLE.value),
        blank=True,
        default=list
    )

    class Meta:
        indexes = [models.Index(fields=['telegram_id']), ]


class UserStage(models.Model):
    telegram_id = models.TextField(max_length=200)
    step = models.CharField(max_length=200)
    step_under = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        indexes = [models.Index(fields=['telegram_id']), ]


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ActivationKey(models.Model):
    activation_key = models.CharField(max_length=150)
