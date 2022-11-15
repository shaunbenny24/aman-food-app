from django.urls import path
from . import views

urlpatterns = [
   
    path ('product/', views.product, name = 'product'),
    path ('product/<int:id>', views.product ,name = 'products'),
    path ('productlist/<int:id>', views.productlist, name = 'productlist'),

]
 

