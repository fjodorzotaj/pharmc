from django.db import models

# Our model below

class Product (models.Model):
	title = models.CharField(max_length=140)
	description = models.TextField()
	price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99) #100.00
	sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=6.99, null=True, blank=True)

	def __unicode__(self): # in python 3 instead of __unicode__ we use __str__(self)
		return self.title
