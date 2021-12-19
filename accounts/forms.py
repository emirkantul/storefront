from django.forms import ModelForm, fields
from django.forms.widgets import DateTimeInput
from accounts.models import  *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model
from django.contrib.admin import widgets
from django import forms

User = get_user_model()

class CustomerProfileForm(ModelForm):
    class Meta:
        model = Customer 
        fields = '__all__'
        exclude = ['date_created', 'user']
class CreateCustomerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2'] 

    def save(self, commit=True):
        user = super(CreateCustomerForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.user_type = 2
        if commit:
            user.save()
        return user
    

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'res', 'date_created', 'done', 'cost', 'status']

    def save(self, cust, res, commit=True):
        order = super(OrderForm, self).save(commit=False)
        order.status = 'Pending'
        order.customer = cust
        order.res = res
        if commit:
            order.save()
        return order
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        exclude = ['customer', 'res', 'date_created', 'status', 'table']

    def save(self, cust, res, commit=True):
        reservation = super(ReservationForm, self).save(commit=False)
        reservation.status = 'Pending'
        reservation.table = '-'
        reservation.customer = cust
        reservation.res = res
        if commit:
            reservation.save()
        return reservation