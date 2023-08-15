from django.urls import path

from jobs.views import home,createjob,jobDetail

app_name = "jobs"
urlpatterns = [
	path('',home,name="home"),
	path('createjob/',createjob,name="createjob"),
	path('detail/<slug:slug>/',jobDetail,name="detail"),
]