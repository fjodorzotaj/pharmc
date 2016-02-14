from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .forms import ProductAddForm
from .models import Product

def create_view(request):
	form = ProductAddForm()
	template = "create_view.html"
	context = {
			"form": form
		}
	return render(request, template, context)

def detail_slug_view(request, slug=None):
	try:
		product = get_object_or_404(Product, slug=slug)
	except Product.MultipleObjectsReturned:
		product = Product.objects.filter(slug=slug).order_by("-title").first()
	template = "detail_view.html"
	context = {
		"object": product
		}
	return render(request, template, context)


def detail_view(request, object_id=None):
	# GET only 1 item
	product = get_object_or_404(Product, id=object_id)
	template = "detail_view.html"
	context = {
		"object": product
		}
	return render(request, template, context)


	# if object_id is not None:
	# 	try:
	# 		product = Product.objects.get(id=object_id)
	# 	except Product.DoesNotExist:
	# 		product = None
	# 	template = "detail_view.html"
	# 	context = {
	# 		"object": product
	# 		}
	# 	return render(request, template, context)
	# else:
	# 	raise Http404

	# if request.user.is_authenticated():
	# 	print request
	# 	product  = Product.objects.all().first()
	# 	template = "detail_view.html"
	# 	context = {
	# 		"object": product
	# 	}
	# else:
	# 	template = "not_found.html"
	# 	context = {}
	# return render(request, template, context)

def list_view(request):
	# GET a list of multiple items
	print request
	queryset = Product.objects.all()
	template = "list_view.html"
	context = {
		"queryset": queryset
	}

	return render(request, template, context)
