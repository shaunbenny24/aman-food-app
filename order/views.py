from django.shortcuts import render
from django.http import HttpResponse
from order.forms import OrderForm
from product.models import Category,Product,OrderItem,Order

# Create your views here.

def orders(request):
    orders = Order.objects.filter(user = request.user)

    return render(request,'order/order.html',{'orders':orders})


def orderlist(request,pk):
    order = Order.objects.get(pk=pk)
    singles = OrderItem.objects.filter(order=order)
    print(singles)
    return render(request,'order/ordersingle.html',{'singles':singles})



def orderconfirm(request):
    return render(request,'order/success.html')