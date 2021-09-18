from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
# import requests



def liked_jobs(request):
    return render(request, 'jobs.html')

def recomended_jobs(request):
    return render(request, 'jobs.html')

def login(request):
    return render(request, 'login.html')

def register(request):

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User account was created!')
            # return redirect('register')

        else:
            messages.error(request, 'Something went wrong!')
            # return redirect('register')


    return render(request, 'register.html', {'form':form})