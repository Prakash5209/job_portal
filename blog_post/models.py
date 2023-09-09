from django.db import models

class Faq_model(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()

	def __str__(self):
		return self.title

class Blog_photo(models.Model):
	title = models.CharField(max_length = 255)
	image = models.ImageField(upload_to="Blog",blank=True,null=True)

	def __str__(self):
		return self.title