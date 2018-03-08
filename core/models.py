from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
