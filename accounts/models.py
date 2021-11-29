from django.db import models
from django.db.models.fields import BooleanField
from django.forms.widgets import Widget
from django.contrib.auth.models import User

# Create your models here.
class User(User):
    USER_TYPE_CHOICES = (
        (1, 'restaurant'),
        (2, 'customer'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

class Customer(models.Model):
    GENDER = ( 
        ('Other', 'Other'),
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    name = models.CharField(max_length=100, null=True)  
    surname = models.CharField(max_length=100, null=True)  
    gender = models.CharField(max_length=100, null=True, choices=GENDER)  
    phone = models.CharField(max_length=100, null=True)  
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    birth = models.DateField(null=True)

    def __str__(self):
        return self.name + " " + self.surname

class Restaurant(models.Model):
    CATEGORY = ( 
        ('Cafe', 'Cafe'),
        ('Fine Dining', 'Fine Dining'),
        ('Casual or Family-Style', 'Casual or Family-Style'),
        ('Fast Food', 'Fast Food'),
        ('Other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    restaurant_name = models.CharField(max_length=100, null=True)  
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)  
    phone = models.CharField(max_length=100, null=True)  
    date_created = models.DateField(auto_now_add=True, null=True)
    address = models.CharField(max_length=200, null=True)  

    def __str__(self):
        return self.restaurant_name

class Reservation(models.Model):
    res_date = models.DateTimeField(null=True)
    table = models.CharField(max_length=100, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    res = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    date_created = models.DateField(auto_now_add=True, null=True)
    done = BooleanField(default=False)

class Order(models.Model):
    order_date = models.DateTimeField(null=True)
    content = models.CharField(max_length=100, null=True)
    cost = models.IntegerField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    res = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    date_created = models.DateField(auto_now_add=True, null=True)
    done = BooleanField(default=False)