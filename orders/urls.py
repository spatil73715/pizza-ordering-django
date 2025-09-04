from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", auth_views.LoginView.as_view(
        template_name="registration/login.html",
        redirect_authenticated_user=True
    ), name="login"),

    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("thank-you/", views.thank_you, name="thank_you"),
    path("add-to-cart/<int:pizza_id>/", views.add_to_cart, name="add_to_cart"),
]
