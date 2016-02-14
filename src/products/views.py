from django.shortcuts import render

def detail_view(request):
	# GET 1 item
	print request
	template = "detail_view.html"
	context = {}

	return render(request, template, context)

def list_view(request):
	# GET a list of multiple items
	print request
	template = "list_view.html"
	context = {}

	return render(request, template, context)
