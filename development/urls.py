from django.contrib import admin
from django.urls import path

from .views import development

urlpatterns = [
    path('', development, name='development')
]