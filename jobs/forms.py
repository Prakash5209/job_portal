from django import forms

from jobs.models import CreateJob

class CreateJobForm(forms.ModelForm):
	class Meta:
		model = CreateJob
		fields = ("image","company_name","job_title","phone","address","website","email","description")

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})