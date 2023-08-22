from django.urls import path

from account.views import userlogin,usersignup,userlogout,profile_view,profile_update_view

app_name="account"
urlpatterns = [
	path('login/',userlogin,name="userlogin"),
	path('signup/',usersignup,name="usersignup"),
	path('logout/',userlogout,name="userlogout"),
    path('profile/<str:username>/',profile_view, name='profile'),
    path('profile-edit/',profile_update_view,name="profile_update"),
]