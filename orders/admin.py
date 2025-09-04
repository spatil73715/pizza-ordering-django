from django.contrib import admin
from .models import Pizza, Order, OrderItem

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")   # show these fields in list
    search_fields = ("name",)                         # search by pizza name

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "is_completed", "payment_method", "created_at")  
    list_filter = ("is_completed", "payment_method")

    inlines = [OrderItemInline]                       # show order items inside order page
