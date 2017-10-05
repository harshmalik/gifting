from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length = 5000)
    phone = models.IntegerField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    query = models.CharField(max_length = 5000)
    class Meta:
        verbose_name_plural = 'Queries (Contact Us)' #Name to be shown in django admin

