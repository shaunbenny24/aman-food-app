from django.shortcuts import render
from django.http import HttpResponse
from product.models import Category,Product
from cart.cart import Cart
# Create your views here.

def index(request):

    products = Product.objects.all()
    categorys = Category.objects.all()
    context = {'products':products,'categorys': categorys}
    return render(request,'index.html',context,)




   
