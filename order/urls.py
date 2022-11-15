from django.urls import path
from . import views

urlpatterns = [
    path ('order/', views.orders, name = 'order'),
    path ('orderlist/<int:pk>/', views.orderlist, name = 'orderlist'),
    path ('ordersuccess/', views.orderconfirm, name = 'success'),

]
 