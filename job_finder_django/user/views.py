from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
# import requests







def liked_jobs(request):
    return render(request, 'jobs.html')

def recomended_jobs(request):
    return render(request, 'jobs.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')