from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
# import requests

from .forms import jobStatsForm, jobFindForm
from .jobs_filter import job_request, filter_offer_info, return_display_info
from .jobs_categories import categories
from .job_skills import all_skills
from .content_based_filter import create_user_skills_dic, sort_all_offers, get_best_offers_and_info


# Create your views here.

def home(request):
    form = jobStatsForm()

    if request.method == 'POST':
        form = jobStatsForm(request.POST)
        if form.is_valid():

            #pass form data to display_stats function
            request.session['form_input'] = form.cleaned_data
            return redirect('display_stats')


    return render(request, 'home.html', {'form': form})



def find_job(request):

    form = jobFindForm()

    if request.method == 'POST':
        form = jobFindForm(request.POST)
        
        if form.is_valid():
            formData = form.cleaned_data

            
            #get all jobs ids and create valid user dictionary
            form_values = formData
            user_skills_list = request.POST.getlist('user_skills_list[]')
            user_skills_dic = create_user_skills_dic(user_skills_list)

            #request
            data = job_request('https://justjoin.it/api/offers')

            sorted_offers = sort_all_offers(data, 30, user_skills_dic, form_values)
            
            personalized_offers = get_best_offers_and_info(sorted_offers, user_skills_dic)

            #create sessions with best jobs info
            request.session['form_values'] = form_values
            request.session['user_skills_list'] = user_skills_list
            request.session['personalized_offers'] = personalized_offers

            return redirect('personalized_offers')
            


    all_skills.sort()


    context = {'skills':all_skills, 'form':form}

    return render(request, 'find_job.html', context)



def display_stats(request):
    form_values = request.session.get('form_input')

    data = job_request('https://justjoin.it/api/offers')

    filtered_data = filter_offer_info(data, categories, form_values)
    
    display_info = return_display_info(filtered_data)

    context = {'data':display_info, 'offers_number':sum(display_info['most_common_cities']['data'])}

    return render(request, 'stats.html', context)


def personalized_offers(request):

    #Get informations

    personalized_offers = request.session.get('personalized_offers')
    form_values = request.session.get('form_values')
    user_skills_list = request.session.get('user_skills_list')

    
    context = {'offers':personalized_offers, 'form_values':form_values, 'user_skills_list':user_skills_list}
    
    

    return render(request, 'personalized_offers.html', context)








def liked_jobs(request):
    return render(request, 'jobs.html')

def recomended_jobs(request):
    return render(request, 'jobs.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')