from .forms import StudentSignUp

from .models import User
from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.

def loginPage(request):
    return render(request, 'smsapp/login.html')
    

def register(request):
    return render(request, 'smsapp/register.html')


class StudentRegister(CreateView):
    model = User
    form_class = StudentSignUp
    template_name = 'smsapp/std_register.html'