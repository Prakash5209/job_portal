from django import forms

from jobs.models import CreateJob

class CreateJobForm(forms.ModelForm):
	class Meta:
		model = CreateJob
		fields = ("image","company_name","job_title","phone","address","website","email","description")