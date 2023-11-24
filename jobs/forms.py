from django import forms
from ckeditor.widgets import CKEditorWidget

from jobs.models import CreateJob,FormContainer

class CreateJobForm(forms.ModelForm):
	class Meta:
		model = CreateJob
		# fields = ("image","company_name","job_title","phone","address","website","email","description","requirements")
		exclude = ("user","slug",)

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})


class FormContainerForm(forms.ModelForm):
	class Meta:
		model = FormContainer
		fields = '__all__'
		# exclude = ['createjob']
		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'content':CKEditorWidget(),
		}


class CustomFormContainer(forms.Form):
	title = forms.CharField()
	content = forms.CharField(widget=CKEditorWidget())

	title.widget.attrs.update({'class':'form-control'})