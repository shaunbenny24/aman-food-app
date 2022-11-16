from django.shortcuts import render, redirect
from django.http import HttpResponse
from .cart import Cart
from order.forms import OrderForm
from product.models import Category,Product,OrderItem,Order
# Create your views here.

def cart(request):
    return render(request,'cart/cart.html')

def checkout(request):
    if request.method=='POST':

        cart = Cart(request)
        form = OrderForm(request.POST)
        if form.is_valid():
            print('item is')
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'])


                cart.clear()
                return redirect('success')
            
    form = OrderForm()

    return render(request,'cart/Checkout.html',{'form':form})


def cart_add(request,pk):
    cart = Cart(request)
    cart.add(pk)

    return redirect('cart')


# def clear(request):
#     cart = Cart(request)
#     cart.clear(pk)


def cart_remove(request,pk):
    cart = Cart(request)
    cart.remove(pk)
    return redirect('cart')