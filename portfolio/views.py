from django.shortcuts import render
from django.http import HttpResponse
from .models import Project # импорт нужен для импорта из базы данных

def home(request):
    projects = Project.objects.all() # данная строка импортирует все данные из базы данных
    return render(request, 'portfolio/home.html', {'projects':projects})

def about(request):
    return render(request, 'portfolio/about.html')
# Create your views here.
