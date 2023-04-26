from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    link_car = models.CharField(max_length=150)
    date = models.DateField()


class AvtoImport(models.Model):
    csv_file = models.FileField(upload_to='uploads/')
    date_added = models.DateTimeField(auto_now_add=True)
