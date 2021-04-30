import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria_project.settings")

import django

django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id, pizza)


p = Pizza.objects.get(id=1)
print(p.pizza_name)
print(p.date_added)

toppings = p.topping_set.all()

for topping in toppings:
    print(topping)

#This works! yayyayay. 
