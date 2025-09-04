from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



@login_required
def home(request):
    pizzas = Pizza.objects.all()
    return render(request, "index.html", {"pizzas": pizzas})



@login_required
def add_to_cart(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    order, created = Order.objects.get_or_create(user=request.user, is_completed=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, pizza=pizza)
    if not created:
        order_item.quantity += 1
    order_item.save()
    return redirect("cart")



@login_required
def cart(request):
    order = Order.objects.filter(user=request.user, is_completed=False).first()
    return render(request, "cart.html", {"order": order})



@login_required
def checkout(request):
    if request.method == "POST":
        online_payment = request.POST.get("online_payment")
        order = Order.objects.filter(user=request.user, is_completed=False).first()

        if order:
            order.online_payment = online_payment
            order.is_completed = True
            order.save()

        if online_payment == "online":
            return redirect("online_payment")  

        return redirect("thank_you")

    return render(request, "checkout.html")



def thank_you(request):
    return render(request, "order_success.html")




def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()          
            login(request, user)          
            return redirect("home")      
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def online_payment(request):
    if request.method == "POST":
        payment_method = request.POST.get("payment_method")
        # You can save this choice to the order or process it later
        order = Order.objects.filter(user=request.user, is_completed=False).first()
        if order:
            order.payment_method = payment_method
            order.save()
        return redirect("thank_you")
    return render(request, "online_payment.html")
