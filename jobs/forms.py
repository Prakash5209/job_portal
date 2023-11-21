from django import forms

from jobs.models import CreateJob,Create_topic,Topic_field,Create_topic

class CreateJobForm(forms.ModelForm):
	class Meta:
		model = CreateJob
		# fields = ("image","company_name","job_title","phone","address","website","email","description","requirements")
		exclude = ("user","slug",)

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})


class Create_topic_Form(forms.ModelForm):
	class Meta:
		model = Create_topic
		fields = '__all__'

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'form-control'})

	

# class Select_title_Form(forms.Form):
# 	title = forms.ModelChoiceField(queryset=Create_topic.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

class Select_title_field_Form(forms.Form):
	fields = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))


# class Topic_field_Form(forms.ModelForm):
# 	class Meta:
# 		model = Topic_field
# 		fields = '__all__'

# 	def __init__(self,*args,**kwargs):
# 		super().__init__(*args,**kwargs)

# 		for field in self.fields:
# 			self.fields[field].widget.attrs.update({'class':'form-control'})