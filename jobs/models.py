from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.utils.text import slugify

from django.conf import settings

class TimeStampModel(models.Model):
	id = models.AutoField(primary_key=True)
	created_at = models.DateTimeField(auto_now_add = True)
	modified_at = models.DateTimeField(auto_now = True)

	class Meta:
		ordering = ['-modified_at','-created_at']
		abstract = True

class CreateJob(TimeStampModel):
	image = models.ImageField(upload_to='posts',blank=True,null=True)
	company_name = models.CharField(max_length=255)
	phone = models.CharField(max_length=10)
	address = models.CharField(max_length=255)
	website = models.CharField(max_length=255,blank=True,null=True)
	email = models.EmailField(max_length=255)
	company_description = models.TextField()
	nationality = models.CharField(max_length=255)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
	slug = models.SlugField(blank=True,null=True)

	job_title = models.CharField(max_length=255)
	def __str__(self):
		return self.company_name
	
	def save(self,*args,**kwargs):
		self.slug = slugify(self.company_name)
		super().save(*args,**kwargs)
		# About_more_job_info.objects.create(createjob = self)

class Create_topic(models.Model):
	createjob = models.ForeignKey(CreateJob,on_delete=models.CASCADE)
	title = models.CharField(max_length=255)

	def __str__(self):
		return self.title
	
class Topic_field(models.Model):
	choose_topic = models.ForeignKey(Create_topic,on_delete=models.CASCADE)
	field = models.CharField(max_length=255)

	def __str__(self):
		return f"{self.choose_topic}-{self.field}"


class ContactusImageMap(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to="map",blank=False,null=False)

