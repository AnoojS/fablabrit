from distutils.command.upload import upload
from email.mime import image
from django.db import models

class Home(models.Model):
    homepage = models.ImageField(upload_to='home/homepage')

class Gallery(models.Model):
    image = models.ImageField(upload_to='home/gallery')
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=150)