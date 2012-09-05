from django.http import HttpResponse
from django.contrib import auth

def trackapp_main(request):
	return HttpResponse("<h1>tRack</h1>")
