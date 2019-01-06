from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	current_time={'hours':1,'minutes':30,'seconds':59}
	return render(request,'ex_application/index.html',current_time)

def register(request):
	return render(request,'ex_application/register.html')
