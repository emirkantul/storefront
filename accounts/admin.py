from django.contrib import admin

# Register your models here.

from .models import Customer, Restaurant, Order, Reservation

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Reservation)
