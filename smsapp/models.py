from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  is_student = models.BooleanField('student status', default=False)
  is_teacher = models.BooleanField('teacher status', default=False)



class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


  def __str__(self):
    return self.user.username

class Student_Admission(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(max_length=200)
    parents_name = models.CharField(max_length=200)

    # student_image = models.ImageField(upload_to="Student_admission")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    # def image_url(self):
    #     if self.student_image:
    #         return self.student_image.url
    #     else:
    #         return ""

class Teacher(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  phone = models.CharField(max_length=200, default=0)
  destination = models.CharField(max_length=200)


  def __str__(self):
    return self.user.username


# Create your models here.

# class User(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default = False)
#     is_admin = models.BooleanField(default= False)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)


# class Student(models.Model):

    #one to one relationship with User  
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # student has their personal email id, phone number, address and parent's name
    
#     std_email = models.EmailField(max_length=254)
#     std_gender = models.CharField(max_length=50)
#     std_phone = models.CharField(max_length=20)
#     std_address = models.CharField(max_length=200)
#     parents_name = models.CharField(max_length=200)
#     objects = models.Manager()


# class Teacher(models.Model):

    #one to one relationship with User  
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # Teachers have their personal email id, phone number, address 
   
    # t_email = models.EmailField(max_length=254)
    # t_phone = models.CharField(max_length=20)
    # t_address = models.CharField(max_length=200)
    # objects = models.Manager()

    