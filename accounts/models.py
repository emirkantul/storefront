from django.db import models

# Create your models here.

class Customer(models.Model):
    GENDER = ( 
        ('Other', 'Other'),
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    name = models.CharField(max_length=100, null=True)  
    surname = models.CharField(max_length=100, null=True)  
    gender = models.CharField(max_length=100, null=True, choices=GENDER)  
    phone = models.CharField(max_length=100, null=True)  
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name + " " + self.surname