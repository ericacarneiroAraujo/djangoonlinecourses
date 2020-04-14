from django.shortcuts import render

# Create your views here.

def base(request):
	return render(request, 'core/base.html', {})

def contact(request):
	return render(request, 'core/contact.html', {})