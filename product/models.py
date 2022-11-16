
from django.db import models
from django.contrib.auth.models import User

# Crea

class Category(models.Model):
    title = models.TextField()
    image = models.ImageField()
  

    def __str__(self):
        return self.title





class Product(models.Model):
    title = models.TextField()
    pimage1 = models.ImageField()
    pimage2 = models.ImageField()
    price = models.IntegerField() 
    disprice =  models.IntegerField() 
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self):
        return self.title




class Order(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    number = models.IntegerField() 
    
 
    def __str__(self):
        return self.customer_name


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

