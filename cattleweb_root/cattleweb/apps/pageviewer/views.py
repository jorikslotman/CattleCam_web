from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'pageviewer/index.html')

def over_ons(request):
    return render(request, 'pageviewer/over_ons.html')

def contact(request):
    return render(request, 'pageviewer/contact.html')
    
def services(request):
    return render(request, 'pageviewer/services.html')

def producten(request):
    return render(request, 'pageviewer/producten.html')
