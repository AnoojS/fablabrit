from pickle import TRUE
from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=40)
    description=models.TextField(max_length=240)
    member1=models.CharField(max_length=40,blank=TRUE)
    member2=models.CharField(max_length=40,blank=TRUE)
    member3=models.CharField(max_length=40,blank=TRUE)
    member4=models.CharField(max_length=40,blank=TRUE)
    member5=models.CharField(max_length=40,blank=TRUE)
    image1=models.ImageField(upload_to='projects')
    image2=models.ImageField(upload_to='projects')
    image3=models.ImageField(upload_to='projects')