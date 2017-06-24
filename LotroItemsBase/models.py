from django.db import models


class BaseItem(models.Model):
    name = models.CharField(max_length=200, default='Unknown')
    description = models.CharField(max_length=500, default='')
