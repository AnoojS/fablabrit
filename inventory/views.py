from django.shortcuts import render,redirect
from django.views.generic import ListView

from .models import (
    Component,
    Material,
    Tool,
)
from .forms import (
    ComponentForm,
    MaterialForm,
    ToolForm,
)

def inventory(request):
    return render(request, 'inventory.html')

class components(ListView):
    model = Component
    template_name = 'components.html'
    context_object_name = 'component'

class materials(ListView):
    model = Material
    template_name = 'materials.html'
    context_object_name = 'material'

class tools(ListView):
    model = Tool
    template_name = 'tools.html'
    context_object_name = 'tool'