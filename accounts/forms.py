from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import orders,customer

class ordersform(ModelForm ):
    class Meta:
    	model = orders
    	fields = '__all__'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = [ 'username','email','password1','password2']
class CreateCustomer1(ModelForm):
	class Meta:
		model= customer
		fields ='__all__'
