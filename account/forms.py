from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from account.models import User,Profile

class AuthForm(AuthenticationForm):
	pass

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username","password1","password2",)

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    class Meta:
        model = Profile
        fields = ("first_name","last_name","email","contact","address","avatar","bio",)