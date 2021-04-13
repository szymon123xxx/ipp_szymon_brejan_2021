from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

def home(request):
    return render(request, 'films/home.html')


def about(request):
    return render(request, 'films/about.html')


def index(request):
    movies = Movies.objects.all()
    return render(request, 'films/index.html', {"movies": movies})

