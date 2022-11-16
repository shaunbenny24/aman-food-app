from django.urls import path
from . import views
from .forms import LoginForm,SignUpForm
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from django.contrib import messages

urlpatterns = [
    path ('', views.index, name = 'home'),
   
    path ('login/' ,views.signin ,name= 'login'),
    path ('logout/' ,views.signout ,name= 'logout'),

    path('signup/',views.signup , name ='signup'),

]
 