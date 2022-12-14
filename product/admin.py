from django.contrib import admin
from .models import Category,Product,Order,OrderItem


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)


class OrderItemInline(admin.TabularInline):
    model =OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
