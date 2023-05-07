from django.shortcuts import render
from .models import Program

def programs(request):
    program=Program.objects.all()
    return render(request,'programs.html',{'program':program})