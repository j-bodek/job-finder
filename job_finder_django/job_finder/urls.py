"""job_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
    path('', include('user.urls')),

    # sumbit email for reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name='reset_password'),
    # send email
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_send_confirmation.html'), name='password_reset_done'),
    # send email with reset instructions
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='set_new_password.html'), name='password_reset_confirm'),
    # send message that password was successfuly reseted
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]


handler404 = 'user.views.error_404'