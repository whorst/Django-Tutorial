from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

'''
Each model has a number of class variabless, each of which represents a database
field in the model.

Each field is represented by an instance of field class. The name of each field
(question_text, pub_date) is the field's name. You can use this in the python code and
the database will use this as the column name.
'''

'''
Question.objects.get(pk=1)

What does the above line of code do? Well, we know Questions is both an object and a model, because it
inherits from the Models class. So, with .object, we look as every single Question object and
the attributes of said objects. Pk is an attribute that is provided by Django. So, we wil look at
EVERY single Question instantiation and determine which one has the attribute pk that matches.

q.choice_set.create(choice_text='Not much', votes=0)

THe above creates a choice objects
'''



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
