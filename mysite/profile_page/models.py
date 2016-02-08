from __future__ import unicode_literals

from django.db import models
from users.models import User
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, blank=True, null=True)
    surname = models.CharField(max_length=70, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=70, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    published = models.CharField(max_length=1, blank=True, null=True)
