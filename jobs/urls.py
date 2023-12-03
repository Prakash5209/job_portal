from django.urls import path

from jobs.views import home,createjob,jobDetail,jobDelete,search_feature,updatejob,contactus,aboutus

app_name = "jobs"
urlpatterns = [
	path('',home,name="home"),
	path('createjob/',createjob,name="createjob"),


	path('detail/<int:id>/',jobDetail,name="detail"),
    path('jobdelete/<int:id>/',jobDelete,name="jobdelete"),
    path('search/',search_feature,name="search_feature"),
    path('update-job/<int:id>/',updatejob,name="updatejob"),
    
    
    path('contact-us/',contactus,name="contactus"),
    path('about-us/',aboutus,name="aboutus"),
]
