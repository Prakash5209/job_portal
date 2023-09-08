from django.shortcuts import render

from blog_post.models import Faq_model,Blog_photo

def blog(request):
	modls = Faq_model.objects.all()
	blog_photo = Blog_photo.objects.all()
	context = {'modls':modls,'Blog_photo':Blog_photo}
	return render(request,'blog.html',context)