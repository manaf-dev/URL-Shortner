from django.db import models

# Create your models here.
class UrlData(models.Model):
    original_url = models.CharField(max_length=256)
    short_url = models.CharField(max_length=15, unique=True)