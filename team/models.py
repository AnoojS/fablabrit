from email.mime import image
from django.db import models

class Team(models.Model):
    image=models.ImageField(upload_to='team')
    name=models.CharField(max_length=60)
    role=models.CharField(max_length=60)
    phone=models.CharField(max_length=60)
    mail=models.CharField(max_length=60)
    whatsapp=models.CharField(max_length=60)