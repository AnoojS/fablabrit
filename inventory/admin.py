from django.contrib import admin

from .models import (
    Component,
    Material,
    Tool,
)

admin.site.register(Component)
admin.site.register(Material)
admin.site.register(Tool)