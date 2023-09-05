from django.db import models

# Create your models here.

class Dish(models.Model):
    DISH_AVAILABILITY_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.CharField(max_length=3, choices=DISH_AVAILABILITY_CHOICES)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('preparing', 'Preparing'),
        ('received', 'Received'),
        ('ready for pickup', 'Ready For Pickup'),
        ('delivered', 'Delivered'),
    ]

    customer_name = models.CharField(max_length=100)
    dishes = models.JSONField()  # Store an array of dishes as JSON
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES)

    def __str__(self):
        return f"Order for {self.customer_name} - {self.get_status_display()}"
