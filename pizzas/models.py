from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pizza_name

    def add_image(self):
        


class Topping(models.Model):
    pizza_name = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "toppings"
        # Okay, this is important so the plural is right? Not totally sure.

    def __str__(self):
        return self.topping_name


class Pizza_Image(models.Model):
    pizza_name = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    pizza_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.pizza_image


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
