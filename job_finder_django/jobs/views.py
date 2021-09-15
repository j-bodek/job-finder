from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.

def home(request):
    return render(request, 'home.html')

def find_job(request):
    return render(request, 'find_job.html')

def liked_jobs(request):
    return render(request, 'jobs.html')

def recomended_jobs(request):
    return render(request, 'jobs.html')

def display_stats(request):
    
    return render(request, 'stats.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')