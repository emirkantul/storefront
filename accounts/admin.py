from django.contrib import admin

# Register your models here.

from .models import Customer, Restaurant, Order, Reservation, CustomUser

admin.site.register(Customer)
admin.site.register(CustomUser)
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Reservation)
