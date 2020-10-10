from django.http import HttpResponse
from django.shortcuts import render
from .models import elastic, velcro, thread

# Create your views here.
def elastic_view(request):
	
	p = elastic.objects.all()

	return render(request, "elastic.html", {'elastics':p})

def velcro_view(request):
	
	v = velcro.objects.all()

	return render(request, "velcro.html", {'velcros':v})

def thread_view(request):
	
	t = thread.objects.all()

	return render(request, "thread.html", {'threads':t})