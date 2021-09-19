from django.shortcuts import render, redirect
import requests
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from .models import Offer, skill_and_sallary
# import requests



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


@login_required(login_url='login')
def logout_user(request): 
    logout(request)
    messages.error(request, 'User logout')
    return redirect('home')



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



@login_required(login_url='login')
def add_like(request):

    if request.method == 'POST':
        #offer model
        
        #get offer info
        values = request.POST
        

        # check if offer is not already in liked 
        try:

                #Get offer by id
            offer = request.user.offer_set.filter(offer_id=values['delete'][1:])
            
            #delete offer
            offer.delete()

            messages.error(request, 'Offer removed from liked')

            #redirect to liked offers
            return redirect('liked_jobs')

        except:

            offer = Offer()

            #add info to offer model
            offer.user = request.user
            offer.offer_type = 'liked'
            offer.offer_id =values['id'][1:]
            offer.title = values['title']
            offer.city = values['city']
            offer.url = str('https://justjoin.it/offers/'+values['id'][1:])
            offer.img = values['img']
            offer.save()

        

            #add skills
            for skill in values.getlist('skill'):
                Skill = skill_and_sallary()
                Skill.owner = offer
                Skill.name = 'skill'
                Skill.content = skill
                Skill.save()

            #add salaries
            for salary in values.getlist('salary'):
                Salary = skill_and_sallary()
                Salary.owner = offer
                Salary.name = 'salary'
                Salary.content = salary
                Salary.save()

            messages.success(request, 'Offer add to liked')

            #redirect to personalized offers
            return redirect('personalized_offers')




@login_required(login_url='login')
def liked_jobs(request):
    user = request.user

    offers_info = []

    offers = user.offer_set.all()

    for single_offer in offers:
        skills = single_offer.skill_and_sallary_set.filter(name='skill')
        sallarys = single_offer.skill_and_sallary_set.filter(name='salary')

        offer_info = {
            'offer_basic':single_offer,
            'skills':skills,
            'sallarys':sallarys
        }
        offers_info.append(offer_info)


        
    context = {'offers_info':offers_info}

    return render(request, 'liked_offers.html', context)

