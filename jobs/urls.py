from django.urls import path

from jobs.views import home,createjob,jobDetail,jobDelete,search_feature,updatejob,contactus,aboutus

app_name = "jobs"
urlpatterns = [
	path('',home,name="home"),
	path('createjob/',createjob,name="createjob"),


	path('detail/<slug:slug>/',jobDetail,name="detail"),
    path('jobdelete/<slug:slug>/',jobDelete,name="jobdelete"),
    path('search/',search_feature,name="search_feature"),
    path('update-job/<slug:slug>/',updatejob,name="updatejob"),
    
      
    path('contact-us/',contactus,name="contactus"),
    path('about-us/',aboutus,name="aboutus"),
]
