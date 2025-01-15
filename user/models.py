
from django.db import models
from rest_framework.pagination import PageNumberPagination

# Create your models here.

userType = (
    (1, 'ADMIN'),
    (2, 'DRIVER'),
    (3, 'SIMPLE'),
)


class User(models.Model):
    telegram_id = models.CharField(max_length=200, null=True, unique=True)
    chat_id = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(choices=userType, default=3)
    step = models.CharField(max_length=200, blank=True, null=True)
    step_under = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        indexes = [models.Index(fields=['telegram_id']), ]

    def __str__(self):
        return self.last_name


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ActivationKey(models.Model):
    activation_key = models.CharField(max_length=150)

    def __str__(self):
        return self.activation_key
