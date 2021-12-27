from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver

@receiver(post_save, sender=CustomUser)
def create_customer(sender, instance, created, ** kwargs):
    if created:
        if instance.user_type == 1:
            Restaurant.objects.create(user=instance)
            res = Restaurant.objects.get(user = instance)
            Menu.objects.create(res = res)
        if instance.user_type == 2:
            Customer.objects.create(user=instance)



@receiver(post_save, sender=CustomUser)
def save_customer(sender, instance, created, ** kwargs):
    if created:
        if instance.user_type == 1:
            instance.restaurant.save()
        if instance.user_type == 2:
            instance.customer.save()