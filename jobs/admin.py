from django.contrib import admin

from jobs.models import CreateJob

@admin.register(CreateJob)
class CreateJobAdmin(admin.ModelAdmin):
	list_display = ("company_name",)
	prepopulated_fields = {"slug":("company_name",)}