from django.db import models

# Create your models here.
class Survey(models.Model):
    description = models.TextField()
    pub_date = models.DateTimeField('date published')

class Question(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_type = models.CharField(max_length=200)  # radio, checkbox, input field, text_field
    answer_description = models.CharField(max_length=200)

class Response(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
