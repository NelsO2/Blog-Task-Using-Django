from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup_user/', views.signup_user, name='signup_user'),
    path('login_user/', views.login_user, name='login_user'),
     path('logout_user/', views.logout_user, name='logout_user')
    
]