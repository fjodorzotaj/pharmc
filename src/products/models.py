from django.db import models

# Our model below

class Product (models.Model):
	title = models.CharField(max_length=140)

	def __unicode__(self): # in python 3 instead of __unicode__ we use __str__(self)
		return self.title
