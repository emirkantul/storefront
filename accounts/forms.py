from django.forms import ModelForm, fields
from accounts.models import  *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


#class CreateUserForm(UserCreationForm):
#    class Meta:
#        model = User 
#        fields = ['username', 'email', 'password1', 'password'] 

class CreateCustomerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2'] 

    def save(self, commit=True):
        user = super(CreateCustomerForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.user_type = 1
        if commit:
            user.save()
        return user