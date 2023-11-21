from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.text import slugify
from django.contrib import messages
from django.forms import formset_factory
import json

from jobs.forms import CreateJobForm,Create_topic_Form,Select_title_field_Form
from jobs.models import CreateJob,ContactusImageMap,Create_topic,Topic_field

formset_fac = formset_factory(Select_title_field_Form,extra = 0)

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
	create_topic_form = Create_topic_Form(request.POST or None)
	formset = formset_fac(request.POST or None,prefix = 'items')

	# if request.method == 'POST':
	# 	print(request.POST.get(f'items-{str(0)}-fields'))

	createjob_model = CreateJob.objects.all()
	# create_topic_models = Create_topic.objects.filter(createjob = max([i.id for i in CreateJob.objects.all()]))

	if form.is_valid():
		obj = form.save(commit = False)
		obj.user = request.user
		obj.save()
		print(obj.id)
		# data = {'name':form.cleaned_data['company_name']}
		data = {'id':obj.id}
		# return redirect('jobs:home')
		messages.add_message(request,messages.SUCCESS,'Job Created!')
		return JsonResponse(data,safe=False)
	
	if request.method == 'POST':
		for i in range(len(formset)):
			fields = request.POST.get(f'items-{str(i)}-fields')
			title_id = request.POST.get('title')
			print(title_id)
			print(fields)
			for j in Create_topic.objects.all():
				if j.title == title_id:
					Topic_field(choose_topic = j,field = fields).save()
					print('saved')
					data_fields = {'status':'success'}
		return JsonResponse(data_fields,safe=False)
		


	context = {
		'form':form,
		'formset':formset,
		'create_topic_form':create_topic_form,
		# 'create_topic_models':create_topic_models,
		'createjob_model':createjob_model,
		}
	return render(request,'cj_form.html',context)


def createjob_topic_creation(request):
	if request.method == 'POST':
		topic_created_id = {}
		max_id = max([i.id for i in CreateJob.objects.all()])
		for i in CreateJob.objects.all():
			if i.id == max_id:
				obj = Create_topic(createjob = i,title = request.POST.get('title'))
				obj.save()
				# topic_created_id['title'] = obj.title
				# topic_created_id['id'] = obj.id
				topic_created_id[obj.id] = obj.title
		
		# title_data = json.dumps(topic_created_id)
		# print(type(title_data))
		return JsonResponse(topic_created_id,safe=False)
		# for i in Create_topic.objects.all():
		# 	if i.id == topic_created_id:
		# 		print(i)
		# print(Create_topic.objects.all())
		# title_data = [i for i in Create_topic.objects.all() if i.id == topic_created_id]
		# return JsonResponse(list(title_data.values()),safe=False)

				# title_data = {'obj':obj}
				# return JsonResponse(title_data,safe=False)
	context = {}
	return render(request,'cj_form.html')




def fetch_topic_creation(request):
	create_topic_model = Create_topic.objects.filter(createjob = max([i.id for i in CreateJob.objects.all()]))
	# topic_field_model = Topic_field.objects.filter(choose_topic = max([i.id for i in Create_topic.objects.all()]))
	# render topic_field in cj_template
	return JsonResponse(list(create_topic_model.values()),safe=False)


def updatejob(request,slug):
	jobs_model = get_object_or_404(CreateJob,slug=slug,user = request.user)
	form = CreateJobForm(request.POST or None,request.FILES or None,instance=jobs_model)
	# formset = formset_fac(request.POST or None,prefix = 'items')

	if form.is_valid():
		obj = form.save(commit = False)
		messages.add_message(request,messages.SUCCESS,'job information Updated!')
		obj.save()
		updated_slug = obj.company_name
		return redirect(reverse('jobs:detail',args=(slugify(obj.company_name),)))
	context = {'form':form,'jobs_model':jobs_model}
	return render(request,'updatejob.html',context)

# @login_required
def jobDetail(request,slug):
	job_detail = CreateJob.objects.get(slug = slug)
	context = {'job_detail':job_detail}
	return render(request,'j_detail.html',context)


# @login_required
# def jobDelete(request,slug):
# 	job_detail = get_object_or_404(CreateJob,slug=slug,user = request.user)
# 	if job_detail:
# 		job_detail.delete()
# 		messages.add_message(request,messages.SUCCESS,'Successful deletion!')
# 		return redirect('jobs:home')
# 	context = {"job_detail":job_detail}
# 	return render(request,'j_detail.html',context)


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

