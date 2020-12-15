from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Answer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. And this is an update")\

