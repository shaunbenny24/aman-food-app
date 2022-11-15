from django.urls import path
from . import views

urlpatterns = [
    path ('cart/', views.cart, name = 'cart'),
    path ('checkout/', views.checkout, name ='checkout'),
    path ('add/<int:pk>', views.cart_add, name ='cart_add'),
    path ('remove/<int:pk>', views.cart_remove, name ='cart_remove'),



]