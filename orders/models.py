from django.db import models
from django.contrib.auth.models import User


class Pizza(models.Model):
    CATEGORY_CHOICES = [
        ('veg', 'Veg'),
        ('nonveg', 'Non-Veg'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='veg')  # NEW FIELD

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza, through="OrderItem")
    address = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    payment_method = models.CharField(
        max_length=20,
        choices=[("cod", "Cash on Delivery"), ("online", "Online Payment")],
        default="cod"
    )

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.pizza.name} x {self.quantity}"

