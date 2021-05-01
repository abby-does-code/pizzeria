from django.urls import path

# Dot tells Python to import the views.py modeul from the same directory
# as the current urls module
from . import views

# Variable app_name helps Django distinguish this urls.py file from
# files of the same name in other apps within the project
app_name = "pizzas"

urlpatterns = [
    # Notes: the first argument is empty string which matches the base URL
    ## The second arugment specifies the funciton name to call in views.
    ### Third argument provides the name 'index' for this URL to refer to later
    path("", views.index, name="index"),
    path("pizzas", views.pizzas, name="pizzas"),
    path("pizza/<int:pizza_id>/", views.pizza, name="pizza"),
    # Individual pizzas
]
