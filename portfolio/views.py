from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
import random

# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request,'portfolio/Home.html', {'projects':projects})
