from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def image(request):
    return render(request, 'image.html')