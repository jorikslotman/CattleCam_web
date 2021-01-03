from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Answer,Response
from django.db.models import Max
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import Accordion,AccordionGroup

class SurveyForm(forms.Form):
    def __init__(self,survey,*args,**kwargs):
        self.title = survey.public_title
        self.desc = survey.public_description
        super(SurveyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = "col-m2-2 font-weight-bold"


        for question in survey.questions:
            if question.published:
                choices_checkbox = ()
                choices_radio = ()
                add_text_field_id = -1
                for answer in question.answers:
                    if answer.published:
                        if answer.answer_type == 'checkbox':
                            choices_checkbox = (*choices_checkbox,(str(answer.id),answer.public_description))
                            if answer.private_description == 'input':
                                add_text_field_id = answer.id
                        if answer.answer_type == 'radio':
                            choices_radio = (*choices_radio,(str(answer.id),answer.public_description))
                            if answer.private_description == 'input':
                                add_text_field_id = answer.id

                        if answer.answer_type == 'input':
                            self.fields[str(answer.id)] = forms.CharField(label=question.question_text,strip=True,required=False)
                        if answer.answer_type == 'textarea':
                            self.fields[str(answer.id)] = forms.CharField(label=question.question_text,widget=forms.Textarea,strip=True,required=False)

                if len(choices_checkbox)>0:
                    self.fields[str(question.id)+'_checkbox'] = forms.MultipleChoiceField(label=question.question_text,choices=choices_checkbox,widget=forms.CheckboxSelectMultiple,required=False)
                if len(choices_radio)>0:
                    self.fields[str(question.id)+'_radio'] = forms.ChoiceField(label=question.question_text,choices=choices_radio,widget=forms.RadioSelect,required=False)
                if add_text_field_id > -1:
                    self.fields[str(add_text_field_id)+'_checkboxinput'] = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control-sm'}),strip=True,required=False,label='')

    def get_Response_list(self):
        response_id = Response.objects.aggregate(Max('submitted_id'))['submitted_id__max']
        if not isinstance(response_id,int):  # if no responses exist
            response_id = 1
        else:
            response_id += 1

        iteration = []
        for k in self.cleaned_data.keys():
            v = self.cleaned_data[k]
            loc_underscore = k.find('_')
            if loc_underscore > -1:  # key is not just answer.id
                field_type = k[loc_underscore+1:]
                if field_type == 'checkboxinput':
                    answer_ids = [k[:loc_underscore]]
                    answer_txt = [v]
                elif field_type == 'checkbox':
                    answer_ids = v
                    answer_txt = []
                    for id in answer_ids:
                        answer_txt.append(Answer.objects.get(pk=id).public_description)
                elif field_type == 'radio':
                    answer_ids = [v]
                    if v != '':
                        answer_txt = [Answer.objects.get(pk=answer_ids[0]).public_description]
                    else:
                        answer_txt = ['']
            else:
                answer_ids = [k]
                answer_txt = [v]
            for i,answer_id in enumerate(answer_ids):
                if answer_txt[i] != '':
                    iteration.append({
                        'Answer' : Answer.objects.get(pk=int(answer_id)),
                        'answer_text':answer_txt[i],
                        'submitted':True,
                        'submitted_id': response_id # get max value
                    })

        return iteration
