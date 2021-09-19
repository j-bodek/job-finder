from django.contrib import admin

# Register your models here.
from .models import Offer, skill_and_sallary

admin.site.register(Offer)
admin.site.register(skill_and_sallary)
