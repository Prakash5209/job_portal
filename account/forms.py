from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from account.models import User

class AuthForm(AuthenticationForm):
	pass

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username","password1","password2")
