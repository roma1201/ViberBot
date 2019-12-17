from django.db import models
from django.conf import settings


class ViberUser(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    viberid = models.CharField(max_length=256, null=True, blank=True)
    api_version = models.CharField(max_length=256, null=True, blank=True)
    language = models.CharField(max_length=256, null=True, blank=True)
    country = models.CharField(max_length=52, null=True, blank=True)
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    is_blocked = models.BooleanField(default=False, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.phone_number}'


# Create your models here.
