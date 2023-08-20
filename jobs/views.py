from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from jobs.forms import CreateJobForm
from jobs.models import CreateJob

def home(request):
	jobs_modl = CreateJob.objects.all()
	# jobs_modl = CreateJob.objects.filter(company_name__icontains = "cloud")
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
		return redirect('jobs:home')
	context = {'form':form}
	return render(request,'cj_form.html',context)

@login_required
def jobDetail(request,slug):
	job_detail = CreateJob.objects.get(slug = slug)
	context = {'job_detail':job_detail}
	return render(request,'j_detail.html',context)


@login_required
def jobDelete(request,slug):
	job_detail = CreateJob.objects.get(slug=slug, user = request.user)
	if job_detail:
		job_detail.delete()
		return redirect('jobs:home')
	context = {"job_detail":job_detail}
	return render(request,'j_detail.html',context)


