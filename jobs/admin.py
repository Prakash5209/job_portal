from django.contrib import admin

from jobs.models import CreateJob,ContactusImageMap,Create_topic,Topic_field

@admin.register(CreateJob)
class CreateJobAdmin(admin.ModelAdmin):
	list_display = ("company_name",)
	prepopulated_fields = {"slug":("company_name",)}


@admin.register(ContactusImageMap)
class ContactusImageMapAdmin(admin.ModelAdmin):
	list_display = ("image",)

admin.site.register(Create_topic)
admin.site.register(Topic_field)