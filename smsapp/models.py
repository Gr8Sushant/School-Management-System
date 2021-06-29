from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default = False)
    is_admin = models.BooleanField(default= False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)


class Student(models.Model):

    #one to one relationship with User  
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # student has their personal email id, phone number, address and parent's name
    
    std_email = models.EmailField(max_length=254)
    std_gender = models.CharField(max_length=50)
    std_phone = models.CharField(max_length=20)
    std_address = models.CharField(max_length=200)
    parents_name = models.CharField(max_length=200)
    objects = models.Manager()


class Teacher(models.Model):

    #one to one relationship with User  
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # Teachers have their personal email id, phone number, address 
   
    t_email = models.EmailField(max_length=254)
    t_phone = models.CharField(max_length=20)
    t_address = models.CharField(max_length=200)
    objects = models.Manager()

    