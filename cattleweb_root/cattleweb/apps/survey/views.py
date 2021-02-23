from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
import datetime
from .models import Survey,Response
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
            for response_data in form.get_Response_list():
                response_object = Response(
                    answer=response_data['Answer'],
                    answer_text=response_data['answer_text'],
                    submitted=response_data['submitted'],
                    submitted_id=response_data['submitted_id'],
                    response_time=datetime.datetime.now()
                )
                response_object.save()
            if survey.next_survey is not None:
                return redirect('survey:assess', survey_id=survey.next_survey.id)
            else:
                return redirect('survey:thanks')


    form = SurveyForm(survey)
    context = {'survey' : survey,'form' : form,}

    return render(request, 'survey/assess.html',context=context)

def thanks(request):
    messages.warning(request, 'HET GAAT FOUT JONGEN')
    messages.success(request, 'Bedankt voor het invullen!')
    return redirect('survey:index')


