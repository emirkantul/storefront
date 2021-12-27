from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField
from django.forms.widgets import Widget
from django.contrib.auth.models import AbstractUser, User
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'restaurant'),
        (2, 'customer'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    def __str__(self):
        return str(self.username)

class Customer(models.Model):
    GENDER = ( 
        ('Other', 'Other'),
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    mail = models.EmailField(null=True)
    name = models.CharField(max_length=100, null=True)  
    surname = models.CharField(max_length=100, null=True)  
    gender = models.CharField(max_length=100, null=True, choices=GENDER)  
    phone = models.CharField(max_length=100, null=True)  
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    birth = models.DateField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return str(self.name + " " + self.surname)

class Restaurant(models.Model):
    CATEGORY = ( 
        ('Cafe', 'Cafe'),
        ('Bar', 'Bar'),
        ('Fine Dining', 'Fine Dining'),
        ('Casual or Family-Style', 'Casual or Family-Style'),
        ('Fast Food', 'Fast Food'),
        ('Other', 'Other'),
    )
    city = models.CharField(max_length=100, null=True)  
    district = models.CharField(max_length=100, null=True)  
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    rating = models.DecimalField(default=10.0, decimal_places=1, max_digits=3)
    restaurant_name = models.CharField(max_length=100, null=True)  
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)  
    phone = models.CharField(max_length=100, null=True)  
    date_created = models.DateField(auto_now_add=True, null=True)
    address = models.TextField(max_length=400, null=True)  
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return str(self.restaurant_name)

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

class Reservation(models.Model):
    STATUS = ( 
        ('Pending', 'Pending'),
        ('Done', 'Done'),
        ('Restaurant Approved', 'Restaurant Approved'),
        ('Restaurant Declined', 'Restaurant Declined'),
    )
    res_date = models.DateTimeField(null=True)
    table = models.CharField(max_length=100, null=True)
    notes = models.TextField(max_length=200, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    res = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    date_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return str(self.customer.name + " res to " + self.res.restaurant_name)

class Order(models.Model):
    STATUS = ( 
        ('Pending', 'Pending'),
        ('Done', 'Done'),
        ('Restaurant Approved', 'Restaurant Approved'),
        ('Restaurant Declined', 'Restaurant Declined'),
    )
    order_date = models.DateTimeField(null=True)
    content = models.TextField(max_length=100, null=True)
    notes = models.TextField(max_length=200, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    res = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    date_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return str(self.customer.name + " order to " + self.res.restaurant_name)

class Menu(models.Model):
    restaurant_name = models.CharField(max_length=100, null=True)
    res = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.restaurant_name)

class MenuElement(models.Model):
    CATEGORY = ( 
        ('Cold Drink', 'Cold Drink'),
        ('Hot Drink', 'Hot Drink'),
        ('Alcohol', 'Alcohol'),
        ('Starter', 'Starter'),
        ('Meat&Fish', 'Meat&Fish'),
        ('Soup', 'Soup'),
        ('Burger', 'Burger'),
        ('Pizza', 'Pizza'),
        ('Pasta', 'Pasta'),
        ('Desert', 'Desert'),
    )
    name = models.CharField(max_length=100, null=True)
    cost = models.IntegerField(null=True)
    ingredients = models.CharField(max_length=200, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    food_category = models.CharField(max_length=100, null=True, choices=CATEGORY)  
    image = models.ImageField(default='default.png', upload_to='')


    def __str__(self):
        return str(self.name)

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    header = models.CharField(max_length=100, null=True)
    comment = models.TextField(max_length=200, null=True)
    rate = models.DecimalField(decimal_places=1, default=10, max_digits=3)
    res = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.customer.name) + " comment to " + str(self.res.restaurant_name)