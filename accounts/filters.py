import django_filters

from .models import *

class RestaurantFilter(django_filters.FilterSet):
    class Meta:
        model = Restaurant
        fields = '__all__'
        exclude = ['user', 'rating', 'date_created', 'phone']

class FoodFilter(django_filters.FilterSet):
    class Meta:
        model = MenuElement
        fields = '__all__'
        exclude = ['cost', 'menu', 'image']