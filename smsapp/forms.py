from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm

from .models import Student, User, Teacher, Student_Admission

class Student_admission_form(ModelForm):
    class Meta:
        model = Student_Admission
        fields = ['username', 'first_name', 'last_name',
                  'address', 'email', 'phone', 'parents_name']

class StudentSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    phone=forms.CharField(required=True)
    desination=forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.phone=self.cleaned_data.get('phone')
        teacher.desination=self.cleaned_data.get('desination')
        teacher.save()

        return teacher

# class StudentSignUp(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     std_email = forms.EmailField(required=True)
#     std_phone = forms.CharField()
#     std_address = forms.CharField(required=True)
#     parents_name = forms.CharField(required=True)

    
#     class Meta(UserCreationForm.Meta):
#         model = User
    
    
#     @transaction.atomic
#     def data_save(self):
#         user = super().save(commit=False)
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.save()
#         student = Student.students.create(user = user)
#         student.email = self.cleaned_data.get('std_email')
#         student.phone = self.cleaned_data.get('std_phone')
#         student.address = self.cleaned_data.get('std_address')
#         student.parents = self.cleaned_data.get('parents_name')

#         student.save()
#         return user
        


# class TeacherSignUp(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     t_email = forms.EmailField(required=True)
#     t_phone = forms.CharField(required=True)
#     t_address = forms.CharField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def data_save(self):
#         user = super().save(commit=False)
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.save()
#         teacher = Teacher.Teachers.create(user = user)
#         teacher.email = self.cleaned_data.get('t_email')
#         teacher.phone = self.cleaned_data.get('t_phone')
#         teacher.address = self.cleaned_data.get('t_address')

#         teacher.save()
#         return user