from django.db import models

# Create your models here.
class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    public_title = models.CharField(max_length=200,default='Vragenlijst')
    public_description = models.TextField(null=True,default='Met deze vragenlijst willen we graag ... ')
    private_title = models.CharField(max_length=200,default='marktonderzoek')
    private_description = models.TextField(null=True,default='Is CattleCam de kip met gouden eieren?')
    pub_date = models.DateTimeField('date published')

    @property
    def questions(self):
        return self.question_set.all()

    def __str__(self):
        return self.private_title

class Question(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    question_text = models.TextField()
    private_description = models.TextField(null=True)
    pub_date = models.DateTimeField('date published')
    @property
    def answers(self):
        return self.answer_set.all()

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_type = models.CharField(max_length=200,default='checkbox')  # radio, checkbox, input, text_field
    public_description = models.CharField(max_length=200,)
    private_description = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.private_description

class Response(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    response_time = models.DateTimeField(auto_now_add=True)
