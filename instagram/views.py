from django.shortcuts import render
from .models import Image

def home(request):
    images = Image.objects.all()
    return render(request, 'instagram/home.html')

def about(request):
    return render(request, 'instagram/about.html')
