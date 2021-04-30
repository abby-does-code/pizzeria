from django.shortcuts import render

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
    pizzas = Pizza.objects.order_by(date_added)
    return render(request, "pizzas")
