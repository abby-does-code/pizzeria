from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.
# When URL request matches the pattern just defined,
# Django looks for a function called index() in the views.py file

# View function takes in information from a request, prepares data needed,
# and then sends the data back to the browser; using template that defines what the page
# looks like.


def index(request):
    """Home page"""
    return render(request, "pizzas/index.html")


def pizzas(request):
    """Shows the user the pizzas"""
    pizzas = Pizza.objects.order_by("-date_added")
    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas.html", context)


def pizza(request, pizza_id):
    """Allows user to view individual pizzas"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()

    context = {"pizza": pizza, "toppings": toppings}

    return render(request, "pizzas/pizza.html", context)
