from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('register/', views.register, name='register'),
]   
