from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect

from .models import Survey
from .forms import SurveyForm


def index(request):
    return render(request, 'survey/index.html')

def assess(request,survey_id):
    try:
        survey = Survey.objects.get(pk=int(survey_id))
    except:
        messages.warning(request, 'Vragenlijst niet gevonden.')
        return redirect('survey:index')

    if request.method == 'POST':
        form = SurveyForm(survey,request.POST)
        # check whether it's valid:
        if form.is_valid():

            return redirect('survey:thanks')


    form = SurveyForm(survey)
    context = {
        'survey' : survey,
        'form' : form,
               }

    return render(request, 'survey/assess.html',context=context)

def thanks(request):
    messages.success(request, 'Bedankt voor het invullen!')
    return redirect('survey:index')

