from django.shortcuts import render

from blog_post.models import Faq_model

def blog(request):
	modls = Faq_model.objects.all()
	context = {'modls':modls}
	return render(request,'blog.html',context)