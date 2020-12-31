from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect

from .models import Survey
# Create your views here.


def index(request):
    return render(request, 'survey/index.html')

def assess(request,survey_id):
    try:
        survey = Survey.objects.get(pk=int(survey_id))
    except:
        messages.warning(request, 'Vragenlijst niet gevonden.')
        return redirect('survey:index')

    context = {'survey' : survey}

    return render(request, 'survey/assess.html',context=context)

def process_survey(request):
    return redirect('survey:index')

