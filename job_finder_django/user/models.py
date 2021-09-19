from django.conf.urls import url
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    offer_type = models.CharField(max_length=200, blank=True, null=True)
    offer_id = models.CharField(max_length=400, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=400, blank=True, null=True)    
    img = models.CharField(max_length=400, blank=True, null=True)    


class skill_and_sallary(models.Model):
    owner = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True) #something like python, react etc
    content = models.TextField(null=True, blank=True) #short description
