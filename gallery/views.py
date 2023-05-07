from django.shortcuts import render
from .models import Gallery

def gallery(request):
    gallery=Gallery.objects.all()
    return render(request, 'gallery.html', {'gallery':gallery})