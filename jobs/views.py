from django.shortcuts import render,redirect

from jobs.forms import CreateJobForm
from jobs.models import CreateJob

def home(request):
	jobs_modl = CreateJob.objects.all()
	context = {'jobs':jobs_modl}
	return render(request,'home.html',context)


def createjob(request):
	form = CreateJobForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit = False)
		obj.user = request.user
		obj.save()
		return redirect('jobs:home')
	context = {'form':form}
	return render(request,'cj_form.html',context)

def jobDetail(request,slug):
	job_detail = CreateJob.objects.get(slug=slug)
	context = {'job_detail':job_detail}
	return render(request,'j_detail.html',context)
