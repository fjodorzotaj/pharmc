from django.shortcuts import render

from .models import Product

def detail_view(request):
	# GET only 1 item
	if request.user.is_authenticated():
		print request
		product  = Product.objects.all().first()
		template = "detail_view.html"
		context = {
			"object": product
		}
	else:
		template = "not_found.html"
		context = {}
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
