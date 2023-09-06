from django.db import models

class Faq_model(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()

	def __str__(self):
		return self.title
