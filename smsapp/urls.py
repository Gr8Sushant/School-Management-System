from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('register/', views.register, name='register'),
    path('studentregistration/', views.StudentRegister.as_view(), name='std_register'),
    path('teacherregistration/', views.TeacherRegister.as_view(), name='teach_register'),
]   
