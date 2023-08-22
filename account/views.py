from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model

from account.forms import AuthForm,UserForm,ProfileForm
from account.models import Profile

User = get_user_model()
var = Profile.objects.all()
print(var)


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


def profile_view(request,username):
    user = get_object_or_404(User,username=username)
    form = None
    if request.user.is_authenticated and request.user.username == username:
        user = request.user
        initial_data = {
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email':user.email,
            }
        form = ProfileForm(instance=user.profile,initial=initial_data)
    context = {'user':user,'form':form}
    return render(request,'profile.html',context)

def profile_update_view(request):
    form = ProfileForm(request.POST or None, request.FILES or None,instance=request.user.profile)
    if form.is_valid():
        user = request.user
        user.first_name = form.cleaned_data.get("first_name")
        user.last_name = form.cleaned_data.get("last_name")
        user.email = form.cleaned_data.get("email")
        user.save()
        form.save()		
        return redirect(reverse("account:profile",args=(request.user.username,)))
    context = {'form':form}
    return render(request,"profile.html",context)