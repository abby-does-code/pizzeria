from django.shortcuts import render
from .models import Pizza, Topping, Comment
import datetime as datetime

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





def comments(request, pizza_id):
    """Allows user to add a comment"""
    # We're going to want a button that creates a link??

    # checking to see if request method is POST
    # and if the submit button was clicked
    if request.method == "POST" and request.POST.get("btn1"):
        # Get whatever is in the box
        comment = request.POST.get("comment")
        comment = Comment.objects.create(
            pizza_id=pizza_id, comment_text=comment, date_added=datetime.date.today()
        )

    pizza = Pizza.objects.get(id=pizza_id)

    comments = Comment.objects.filter(pizza=pizza_id)

    context = {"pizza": pizza, "comments": comments}

    return render(request, "pizzas/comments.html", context)


