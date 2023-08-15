from django.urls import path

from account.views import userlogin,usersignup,userlogout

app_name="account"
urlpatterns = [
	path('login/',userlogin,name="userlogin"),
	path('signup/',usersignup,name="usersignup"),
	path('logout/',userlogout,name="userlogout"),
]