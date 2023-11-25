from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.text import slugify
from django.contrib import messages
from django.forms import formset_factory
import json

from jobs.forms import CreateJobForm,FormContainerForm,CustomFormContainer
from jobs.models import CreateJob,ContactusImageMap,FormContainer

def home(request):
	jobs_modl = CreateJob.objects.all()		
	context = {'jobs':jobs_modl}
	return render(request,'home.html',context)

def search_feature(request):
	if request.method == 'POST':
		search_query = request.POST.get('search_query')
		jobs_modl = CreateJob.objects.filter(Q(company_name__icontains=search_query) | Q(job_title__icontains=search_query))
		context = {'query':search_query,'searched':jobs_modl}
		return render(request,'home.html',context)
	
@login_required
def createjob(request):
	form = CreateJobForm(request.POST or None,request.FILES or None)
	second_form = CustomFormContainer(request.POST or None)
	modl = CreateJob.objects.all()
	# formset = formset_fac(request.POST or None,prefix = 'items')

	createjob_max_id = max([i.id for i in modl])

	createjob_model = CreateJob.objects.all()

	if form.is_valid():
		obj = form.save(commit = False)
		obj.user = request.user
		obj.save()
		print(obj.id)
		messages.add_message(request,messages.SUCCESS,'Job Created!')
		return JsonResponse({'status':'success'},safe=False)
	
	if request.method == 'POST':
		name = request.POST.get('title')
		content = request.POST.get('content')
		for i in modl:
			if i.id == createjob_max_id:
				FormContainer(createjob=i,title=name,content=content).save()
				print('saved')
				return redirect('jobs:home')
				# return JsonResponse({'status':'success'},safe=False)


	context = {
		'form':form,
		'second_form':second_form,
		'createjob_model':createjob_model,
		}
	return render(request,'cj_form.html',context)

def updatejob(request,slug):
	jobs_model = get_object_or_404(CreateJob,slug=slug,user = request.user)
	form = CreateJobForm(request.POST or None,request.FILES or None,instance=jobs_model)

	formContainermodel = FormContainer.objects.get(createjob = jobs_model.id)
	print('choosen one',formContainermodel.id)

	# formcontainer_choose_one = FormContainer.objects.get(id = 10)

	


	customformcontainer = CustomFormContainer(initial={'title':formContainermodel.title,'content':formContainermodel.content})

	if form.is_valid():
		obj = form.save(commit = False)
		messages.add_message(request,messages.SUCCESS,'job information Updated!')
		obj.save()
		updated_slug = obj.company_name
		return JsonResponse({'status':'success'},safe=False)
		# return redirect(reverse('jobs:detail',args=(slugify(obj.company_name),)))
	
	if request.method == 'POST':
		formContainermodel.title = request.POST.get('title')
		formContainermodel.content = request.POST.get('content')
		formContainermodel.save()
		print('saved')
		return redirect(reverse("jobs:detail",args=(jobs_model.slug,)))
			# formContainermodel.title = customformcontainer.cleaned_dadta['title']
			# formContainermodel.content = customformcontainer.cleaned_data['content']
			# print(formContainermodel.title)
			# print(formContainermodel.content)	
			# # formContainermodel.save()
			# return JsonResponse({'status':'success'},safe=False)
		
	context = {
		'form':form,
		'jobs_model':jobs_model,
		'customformcontainer':customformcontainer,
		'formContainermodel':formContainermodel
		}
	return render(request,'updatejob.html',context)

# @login_required
def jobDetail(request,slug):
	job_detail = CreateJob.objects.get(slug = slug)
	modl = CreateJob.objects.all()
	formcontainer = FormContainer.objects.filter(createjob=job_detail.id)

	context = {
		'job_detail':job_detail,
		'formcontainer':formcontainer,
	}
	return render(request,'j_detail.html',context)

@login_required
def jobDelete(request,slug):
	slug = request.POST.get('slug')
	print(f"my slug==================={slug}")
	post = get_object_or_404(CreateJob,slug = slug,user = request.user)
	post.delete()
	messages.add_message(request,messages.SUCCESS,'post deleted')
	return redirect(reverse('jobs:home'))


def contactus(request):
	# contactimagemap = ContactusImageMap.objects.all()
	contact_Texts = "If you have any questions or comments, we would very much like to hear from you. We value your comments, complaints, and suggestions."
	notes = [
		'For Further information on our services and the JobsNepal.com system, please use the form below or email:',
		'For support and technical questions, please contact our support team: support@sabaikojobs.com',
		'For Sales and Marketing questions, please contact our sales team: info@sabaikojobs.com'
	]
	contact_calls = 'You can also call us during business hours in Nepal at: (977-1) xxxxxxx/ xxxxxxx (Sunday-Friday)'
	context = {
		'contact_Texts':contact_Texts,
		'notes':notes,
		'contact_calls':contact_calls,
		# 'contactimagemap':contactimagemap,
	}
	return render(request,'contactus.html',context)


def aboutus(request):
	title = "Welcome to the sabaikojobs.com"
	first_para = "Welcome to sabaikojobs.com, the largest locally focused employment website in the nation! Our mission is to lead the Internet employment industry in Nepal by providing innovative information, superior resume management software and a comprehensive selection of services."
	second_para = "sabaikojobs.com offers services to the recruiting and job-seeking community in Nepal. We are the only recruitment service provider with 100% free service to all the jobseekers."
	third_para = "It is our mission to bring the burgeoning Nepalese Internet and computing talent to bear on international Web development."
	context = {
		'title':title,
		'first_para':first_para,
		'second_para':second_para,
		'third_para':third_para,
	}
	return render(request,'aboutus.html',context)

