from django.shortcuts import render
from django.http import HttpResponse
from product.models import Category,Product
from cart.cart import Cart
from .forms import LoginForm,SignUpForm
from django.contrib.auth import login,authenticate,logout

from django.contrib import messages
# Create your views here.

def index(request):

    products = Product.objects.all()
    categorys = Category.objects.all()
    context = {'products':products,'categorys': categorys}
    return render(request,'index.html',context,)
    

def signin(request):
   
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                print(user)
                print(password)
                login(request,user)
                return render(request,'index.html')
            else:
                pass


    form = LoginForm()
    return render(request,'login.html',{'form':form})


def signout(request):
    logout(request)


def signup(request):
    if request.method == 'POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.set_password(
                form.cleaned_data['password']
            )
            user.save()
            login(request,user)
            return render(request, 'index.html')


            
            
      
        else:
          
            return render(request, 'signup.html',{'form':form})
            # return HttpResponse('user exists')
        
    sign = SignUpForm()
    print('this is from login',sign)
    return render(request, 'signup.html',{'sign':sign})


   
