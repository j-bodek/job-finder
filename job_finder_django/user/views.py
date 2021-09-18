from django.shortcuts import render, redirect
import requests
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# import requests



def liked_jobs(request):
    return render(request, 'jobs.html')

def recomended_jobs(request):
    return render(request, 'jobs.html')

def login_user(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']


        try:
            user = User.objects.get(email=email)
            username = user.get_username()
        except:
            messages.error(request, 'Ups.. email does not exist')

        user = authenticate(request, username = username, password = password)
        print(user)

        if user:
            login(request, user)
            messages.success(request, 'Welcome Back!')
            return redirect('home')
        else:
            messages.error(request, 'Ups.. email or password is incorrect')


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