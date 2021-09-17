from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
# import requests

from .forms import jobStatsForm, jobFindForm
from .jobs_filter import job_request, filter_offer_info, return_display_info
from .jobs_categories import categories
from .job_skills import all_skills


# Create your views here.

def home(request):
    form = jobStatsForm()

    if request.method == 'POST':
        form = jobStatsForm(request.POST)
        if form.is_valid():

            #pass form data to display_stats function
            request.session['web_input'] = form.cleaned_data
            return redirect('display_stats')


    return render(request, 'home.html', {'form': form})



def find_job(request):

    form = jobFindForm()

    if request.method == 'POST':
        form = jobFindForm(request.POST)
        
        if form.is_valid():
            formData = form.cleaned_data
            print(formData)
            print(request.POST.getlist('mylist[]'))

            #pass form data to display_stats function
            #request.session['web_input'] = form.cleaned_data
            return redirect('personalized_offers')
            


    all_skills.sort()
    context = {'skills':all_skills, 'form':form}

    return render(request, 'find_job.html', context)



def display_stats(request):
    form_values = request.session.get('web_input')

    data = job_request('https://justjoin.it/api/offers')

    filtered_data = filter_offer_info(data, categories, form_values)
    
    display_info = return_display_info(filtered_data)

    context = {'data':display_info, 'offers_number':sum(display_info['most_common_cities']['data'])}

    return render(request, 'stats.html', context)


def personalized_offers(request):
    return render(request, 'personalized_offers.html')



def liked_jobs(request):
    return render(request, 'jobs.html')

def recomended_jobs(request):
    return render(request, 'jobs.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')