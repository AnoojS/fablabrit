from django.shortcuts import render
from services.models import Service

def dashboard(request):
    service=Service.objects.all()
    return render(request,'dashboard.html',{'service':service})