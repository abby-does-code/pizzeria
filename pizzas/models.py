from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_type = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pizza_type

    


"""class Toppings():"""
