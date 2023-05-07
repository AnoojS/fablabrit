from django.db import models


class Component(models.Model):
    item = models.CharField(max_length=120)
    description = models.CharField(max_length=220)
    quantity = models.IntegerField()


class Material(models.Model):
    item = models.CharField(max_length=120)
    description = models.CharField(max_length=220)
    quantity = models.IntegerField()


class Tool(models.Model):
    item = models.CharField(max_length=120)
    description = models.CharField(max_length=220)
    quantity = models.IntegerField()