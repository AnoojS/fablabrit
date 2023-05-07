from django.shortcuts import render

def development(request):
    return render(request,'development.html')