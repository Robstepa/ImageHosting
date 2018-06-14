from django.db import models


# Create your models here.

class Photo(models.Model):
    image = models.ImageField()
    statistic = models.CharField(max_length=500, default=0)
