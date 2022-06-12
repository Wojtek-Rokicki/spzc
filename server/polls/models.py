import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class FirstPoll(models.Model):
    def __str__(self):
        return self.email
    
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

