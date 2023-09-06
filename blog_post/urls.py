from django.urls import path

from blog_post.views import blog

app_name = "blog_post"
urlpatterns = [
	path('articles/',blog,name="articles"),
]