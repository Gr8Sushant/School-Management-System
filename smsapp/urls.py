from django.urls import path
from . import views

#url patterns

urlpatterns =[
    path('', views.login, name='login' ),
]