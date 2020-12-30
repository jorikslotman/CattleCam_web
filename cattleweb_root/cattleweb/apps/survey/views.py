from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Answer

def index(request):
    return render(request, 'survey/index.html')

def assess(request):
    return render(request, 'survey/assess.html')


