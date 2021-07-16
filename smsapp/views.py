# from .forms import StudentSignUp, TeacherSignUp
from .models import User
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import StudentSignUpForm,TeacherSignUpForm, Student_admission_form
from .models import User,Student

def register(request):
	return render(request,'smsapp/register.html')


class StudentRegister(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'smsapp/std_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render('smsapp/std_register.html')


def student_admission(request):
    form = Student_admission_form(request.POST, request.FILES)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('student_admission')

    context = {'form': form}
    return render(request, 'smsapp/std_admission.html', context)


class TeacherRegister(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'smsapp/teach_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('main')

# def loginPage(request):
#     return render(request, 'smsapp/login.html')
    

# def register(request):
#     return render(request, 'smsapp/register.html')


# class StudentRegister(CreateView):
#     model = User
#     # form_class = StudentSignUp
#     template_name = 'smsapp/std_register.html'

# class TeacherRegister(CreateView):
#     model = User
#     # form_class = TeacherSignUp
#     template_name = 'smsapp/teach_register.html'