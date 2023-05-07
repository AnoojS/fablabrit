from pickle import TRUE
from django.shortcuts import render
from .models import Project

def projects(request):
    project=Project.objects.all()
    return render(request,'projects.html',{'project':project})