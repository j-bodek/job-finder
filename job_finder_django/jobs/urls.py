from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('find_job/', views.find_job, name='find_job'),
    path('display_stats/', views.display_stats, name='display_stats'),
    path('personalized_offers/', views.personalized_offers, name='personalized_offers'),
]
