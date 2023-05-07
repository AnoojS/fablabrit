from django.shortcuts import render

from .models import Home,Gallery
from services.models import Service
from team.models import Team


def home(request):
    home = Home.objects.all()
    gallery = Gallery.objects.all()
    service = Service.objects.all()
    team = Team.objects.all()
    return render(request, 'index.html',{'home':home,'gallery':gallery,'service':service,'team':team})