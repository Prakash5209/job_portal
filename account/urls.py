from django.urls import path

from account.views import userlogin,usersignup,userlogout,profile_view,profile_update_view,reset_password

app_name="account"
urlpatterns = [
	path('login/',userlogin,name="userlogin"),
	path('signup/',usersignup,name="usersignup"),
	path('logout/',userlogout,name="userlogout"),
    path('profile/<int:username_id>/',profile_view, name='profile'),
    path('profile-edit/',profile_update_view,name="profile_update"),
	path('reset_password/',reset_password,name='reset_password'),
]