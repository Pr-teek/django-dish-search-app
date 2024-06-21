from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        unique_together = ("name", "restaurant")

    def __str__(self):
        return f"{self.name} at {self.restaurant}"
