from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.text import slugify
from django.contrib import messages

from jobs.forms import CreateJobForm
from jobs.models import CreateJob

def home(request):
	jobs_modl = CreateJob.objects.all()
	context = {'jobs':jobs_modl}
	return render(request,'home.html',context)

def search_feature(request):
	if request.method == 'POST':
		search_query = request.POST['search_query']
		jobs_modl = CreateJob.objects.filter(Q(company_name__icontains=search_query) | Q(job_title__icontains=search_query))
		context = {'query':search_query,'searched':jobs_modl}
		return render(request,'home.html',context)

@login_required
def createjob(request):
	form = CreateJobForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		obj = form.save(commit = False)
		obj.user = request.user
		obj.save()
		messages.add_message(request,messages.SUCCESS,'Job Created!')
		return redirect('jobs:home')
	context = {'form':form}
	return render(request,'cj_form.html',context)

def updatejob(request,slug):
	jobs_model = get_object_or_404(CreateJob,slug=slug,user = request.user)
	form = CreateJobForm(request.POST or None,request.FILES or None,instance=jobs_model)
	if form.is_valid():
		obj = form.save(commit = False)
		messages.add_message(request,messages.SUCCESS,'job information Updated!')
		obj.save()
		updated_slug = obj.company_name
		# print(f"saved slug======================",obj.company_name)
		# print(f"saved slugify======================",slugify(obj.company_name))
		return redirect(reverse('jobs:detail',args=(slugify(obj.company_name),)))
	context = {'form':form,'jobs_model':jobs_model}
	return render(request,'updatejob.html',context)

@login_required
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
	}
	return render(request,'contactus.html',context)

