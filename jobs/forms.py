from django import forms

from jobs.models import CreateJob

class CreateJobForm(forms.ModelForm):
	class Meta:
		model = CreateJob
		fields = ("company_name","phone","address","website","email","description","slug")