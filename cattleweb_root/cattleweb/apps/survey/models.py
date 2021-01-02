from django.db import models

# Create your models here.
class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    public_title = models.CharField(max_length=200,default='Vragenlijst')
    public_description = models.TextField(null=True,default='Met deze vragenlijst willen we graag ... ')
    order_num = models.IntegerField(null=True,default=1)
    private_title = models.CharField(max_length=200,default='marktonderzoek')
    private_description = models.TextField(null=True,default='Is CattleCam de kip met gouden eieren?')
    pub_date = models.DateTimeField('date published')

    @property
    def questions(self):
        return self.question_set.order_by('order_num').all()

    def __str__(self):
        return self.private_title

class Question(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    question_text = models.TextField()
    private_description = models.TextField(null=True)
    order_num = models.IntegerField(default=1)

    @property
    def answers(self):
        return self.answer_set.order_by('order_num').all()

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    ANSWER_TYPES = [
        ('radio','Radio button'),
        ('checkbox','Checkbox'),
        ('input','Input'),
        ('textarea','Text field'),
    ]
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_type = models.CharField(max_length=200,choices=ANSWER_TYPES,default='checkbox')
    public_description = models.CharField(max_length=200,)
    private_description = models.CharField(null=True,max_length=200)
    order_num = models.IntegerField(default=1)

    def __str__(self):
        return self.private_description

class Response(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    response_time = models.DateTimeField(auto_now_add=True)
    submitted = models.BooleanField(default=False)
