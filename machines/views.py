from django.shortcuts import render

def machines(request):
    return render(request, 'machines.html')