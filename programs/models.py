from email.mime import image
from django.db import models

class Program(models.Model):
    title=models.CharField(max_length=40)
    image=models.ImageField(upload_to='programs')
    description=models.TextField(max_length=500)