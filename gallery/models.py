from django.db import models

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=150)