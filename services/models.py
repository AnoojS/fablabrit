from django.db import models

class Service(models.Model):
    image = models.ImageField(upload_to='services')
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=150)