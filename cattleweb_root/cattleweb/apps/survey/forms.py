from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SurveyForm(forms.Form):
    def __init__(self,survey,*args,**kwargs):
        self.title = survey.public_title
        self.desc = survey.public_description
        super(SurveyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False


        for question in survey.questions:
            choices_checkbox = ()
            choices_radio = ()
            add_text_field = False
            for answer in question.answers:
                if answer.answer_type == 'checkbox':
                    choices_checkbox = (*choices_checkbox,(str(answer.id),answer.public_description))
                    if answer.private_description == 'input':
                        add_text_field = True
                if answer.answer_type == 'radio':
                    choices_radio = (*choices_radio,(str(answer.id),answer.public_description))
                    if answer.private_description == 'input':
                        add_text_field = True

                if answer.answer_type == 'input':
                    self.fields[str(question.id)+'_input'] = forms.CharField(label=question.question_text,empty_value=answer.public_description,strip=True,required=False)
                if answer.answer_type == 'textarea':
                    self.fields[str(question.id)+'_input'] = forms.CharField(label=question.question_text,widget=forms.Textarea,strip=True,required=False)

            if len(choices_checkbox)>0:
                self.fields[str(question.id)+'_checkbox'] = forms.MultipleChoiceField(label=question.question_text,choices=choices_checkbox,widget=forms.CheckboxSelectMultiple,required=False)
                self.fields[str(question.id)+'_checkbox'].widget.attrs.update({'class' : 'form-check'})
            if len(choices_radio)>0:
                self.fields[str(question.id)+'_radio'] = forms.ChoiceField(label=question.question_text,choices=choices_radio,widget=forms.RadioSelect,required=False)
                self.fields[str(question.id)+'_radio'].widget.attrs.update({'class' : 'form-check'})
            if add_text_field:
                self.fields[str(question.id)+'_input'] = forms.CharField(label='',strip=True,required=False)


