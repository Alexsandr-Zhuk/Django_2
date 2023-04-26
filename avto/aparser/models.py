from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    link_car = models.CharField(max_length=150)
    date = models.DateField()


