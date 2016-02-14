from django.shortcuts import render

from .models import Product

def detail_view(request):
	# GET 1 item
	print request
	product  = Product.objects.all().first()
	template = "detail_view.html"
	context = {
		"product": product
	}

	return render(request, template, context)

def list_view(request):
	# GET a list of multiple items
	print request
	queryset = Product.objects.all()
	template = "list_view.html"
	context = {
		"queryset": queryset
	}

	return render(request, template, context)
