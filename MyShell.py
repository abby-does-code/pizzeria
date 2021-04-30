import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria_project.settings")

import django

django.setup()

from pizzas.models import Pizza

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id, pizza)
