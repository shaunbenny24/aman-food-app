from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Product
from django.shortcuts import render,get_object_or_404
# Create your views here.

def product(request,id=None):
 
    if id:
        category = get_object_or_404(Category,id=id)
        descrips = Product.objects.filter( Category  = category)

        return render(request,'product/products.html',{'descrips':descrips} )

    else:
            descrips =Product.objects.all()
            return render(request,'product/products.html',{'descrips':descrips}  )

def productlist(request,id):

    productdetail = Product.objects.get(id=id)
        
    return render(request,'product/productsingle.html',{'productdetail':productdetail})





