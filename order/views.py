from django.shortcuts import render
from django.http import HttpResponse
from order.forms import OrderForm
from product.models import Category,Product,OrderItem,Order

# Create your views here.

def order(request):
    orders = OrderItem.objects.all()

    return render(request,'order/order.html',{'orders':orders})


def orderlist(request,id):
    order = Order.objects.get(id=id)
    singles =OrderItem.objects.filter(order=Order)
    return render(request,'order/ordersingle.html',{'singles':singles})



def orderconfirm(request):
    return render(request,'order/success.html')