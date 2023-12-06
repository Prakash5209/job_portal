from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.contrib import messages

from account.forms import AuthForm,UserForm,ProfileForm,Reset_password_Form
from account.models import Profile
from jobs.models import CreateJob

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
		user = form.save()
		Profile.objects.create(user = user)
		return redirect("account:userlogin")
	context = {'form':form}
	return render(request,'signup.html',context)

def userlogout(request):
	logout(request)
	return redirect(reverse("jobs:home"))


def profile_view(request,pk):
	user = get_object_or_404(User,id = pk)
	profile = get_object_or_404(Profile,user = user)
	pro = Profile.objects.all()
	create_jobs = CreateJob.objects.filter(user = pk)
	initial_data = {
		'first_name':user.first_name,
		'last_name':user.last_name,
		'email':user.email,
	}
	form = ProfileForm(request.POST or None,request.FILES or None, instance=profile,initial = initial_data)

	if form.is_valid():
		user = request.user
		user.first_name = form.cleaned_data['first_name']
		user.last_name = form.cleaned_data['last_name']
		user.email = form.cleaned_data['email']
		user.save()
		form.save()
		return redirect('jobs:home')
	context = {
			'user':user,
			'form':form,
			'profile':profile,
			'pro':pro,
			'create_jobs':create_jobs,
		}
	return render(request,'profile.html',context)
	

def reset_password(request):
	form = Reset_password_Form(request.POST or None)
	if request.method == 'POST':
		username1 = request.POST.get('username')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		print(username1,password1,password2)
		# user = User.objects.get(username = username1)
		user = get_object_or_404(User,username = username1)

		if user.username == request.user.username:
			if password1 == password1:
				user.set_password(password2)
				user.save()
				messages.add_message(request,messages.SUCCESS,'password updated')
				return redirect(reverse("account:userlogin"))
			else:
				print('password didn\'t match')
		else:
			print('username didn\nt match')
	context = {'form':form}
	return render(request,'reset_password.html',context)

