from django.contrib import admin
from django.urls import path

from .views import machines

urlpatterns = [
    path('', machines, name='machines')
]