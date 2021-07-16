from django.contrib import admin
from django.urls import path, include
from . import views
from .views import student_admission

urlpatterns = [
    # path('', views.loginPage, name="login"),
    path('', views.register, name='register'),
    path('studentregistration/', views.StudentRegister.as_view(), name='std_register'),
    path('teacherregistration/', views.TeacherRegister.as_view(), name='teach_register'),
    path('admission_form/', student_admission, name='student_admission'),
]   
