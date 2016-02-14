from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Our model below

class Product (models.Model):
	title = models.CharField(max_length=140)
	slug = models.SlugField(blank=True)   # (unique=true)
	description = models.TextField()
	price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99) #100.00
	sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=6.99, null=True, blank=True)

	def __unicode__(self): # in python 3 instead of __unicode__ we use __str__(self)
		return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.title)

pre_save.connect(product_pre_save_receiver, sender=Product)





# def product_post_save_receiver(sender, instance, *args, **kwargs):
# 	if instance.slug != slugify(instance.title):
# 		instance.slug = slugify(instance.title)
# 		instance.save()

# post_save.connect(product_post_save_receiver, sender=Product)