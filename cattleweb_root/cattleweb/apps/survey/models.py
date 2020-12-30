from django.db import models

class VisitEvent(models.Model):
    event_date = models.DateTimeField('event date')
    event_description = models.CharField(max_length=200)

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
    answer_text = models.CharField(max_length=200)

    def save_answer(self):
        Answer.save()