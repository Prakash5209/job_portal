from django.shortcuts import render

from blog_post.models import Faq_model

def blog(request):
	modl = Faq_model.objects.all()
	context = {'modl':modl}
	return render(request,'blog.html',context)