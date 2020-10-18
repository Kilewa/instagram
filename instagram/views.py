from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image



@login_required
def home(request):
    images = Image.objects.all()
    return render(request, 'instagram/home.html')
