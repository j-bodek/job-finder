from django.urls import path
from . import views

urlpatterns = [
    path('liked_jobs/', views.liked_jobs, name='liked_jobs'),
    path('add_like/', views.add_like, name='add_like'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
]
