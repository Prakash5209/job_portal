from django import forms
from django.forms import modelformset_factory

from jobs.models import CreateJob

class CreateJobForm(forms.ModelForm):
	class Meta:
		model = CreateJob
		# fields = ("image","company_name","job_title","phone","address","website","email","description","requirements")
		exclude = ("user","slug",)

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})


# CreateJobFormSet = modelformset_factory(
# 	CreateJob, fields = ("requirements",), extra = 0
# )