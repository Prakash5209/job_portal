from django.contrib import admin

from jobs.forms import FormContainerForm
from jobs.models import CreateJob,ContactusImageMap,FormContainer

@admin.register(CreateJob)
class CreateJobAdmin(admin.ModelAdmin):
	list_display = ('company_name','address','website','nationality',)
	search_fields = ("company_name",'address','website','nationality',)
	prepopulated_fields = {"slug":("company_name",)}


@admin.register(ContactusImageMap)
class ContactusImageMapAdmin(admin.ModelAdmin):
	list_display = ("image",)


class FormContainerModelAdmin(admin.ModelAdmin):
	form = FormContainerForm

@admin.register(FormContainer,FormContainerModelAdmin)
class FormContainer(admin.ModelAdmin):
	list_display = ('createjob','title','content',)
	search_fields = ('createjob','title','content',)
