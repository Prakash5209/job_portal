from django.urls import path

from jobs.views import home,createjob,jobDetail,jobDelete,search_feature,updatejob,contactus,aboutus,createjob_topic_creation,fetch_topic_creation

app_name = "jobs"
urlpatterns = [
	path('',home,name="home"),
	path('createjob/',createjob,name="createjob"),
    path('createjob_topic_creation/',createjob_topic_creation,name='createjob_topic_creation'),

    # path('createjob/',createjob_topic_creation_fields,name='createjob_topic_creation_fields'),

    # fetch api url
    path('fetch_topic_creation/',fetch_topic_creation,name="fetch_topic_creation"),

	path('detail/<slug:slug>/',jobDetail,name="detail"),
    path('jobdelete/<slug:slug>/',jobDelete,name="jobdelete"),
    path('search/',search_feature,name="search_feature"),
    path('update-job/<slug:slug>/',updatejob,name="updatejob"),
    
      
    path('contact-us/',contactus,name="contactus"),
    path('about-us/',aboutus,name="aboutus"),
]
