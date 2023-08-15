from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model

from account.forms import AuthForm,UserForm

User = get_user_model()

def userlogin(request):
	form = AuthForm(request.POST or None)
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user:
			login(request,user)
			return redirect("jobs:home")
		else:
			return redirect("account:userlogin")
	context = {'form':form}
	return render(request,'login.html',context)


def usersignup(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("account:userlogin")
	context = {'form':form}
	return render(request,'signup.html',context)

def userlogout(request):
	logout(request)
	return redirect("jobs:home")