from django.contrib import admin
from django.urls import path

from .views import (
    inventory,

    components,
    materials,
    tools,
)

urlpatterns = [
    path('', inventory, name='inventory'),

    path('components', components.as_view(), name='components'),
    path('materials', materials.as_view(), name='materials'),
    path('tools', tools.as_view(), name='tools'),
]