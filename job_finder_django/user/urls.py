from django.urls import path
from . import views

urlpatterns = [
    path('liked_jobs/', views.liked_jobs, name='liked_jobs'),
    path('recomended_jobs/', views.recomended_jobs, name='recomended_jobs'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
]
