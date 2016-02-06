from __future__ import unicode_literals

from django.db import models


class Privilege(models.Model):
	privilege_name = models.CharField(max_length=64)

class User(models.Model):
	privilege = models.ForeignKey(Privilege, on_delete=models.CASCADE)
	login = models.CharField(max_length=64)
	password = models.CharField(max_length=64)
	email = models.CharField(max_length=255)
	last_visit_date = models.DateTimeField(blank=True, null=True)
    
    