from django.db import models
from django.utils import timezone
import datetime


class Survey(models.Model):
    """Class to encapsulate Survey entity
    Attributes:
        name: character field with max_length=200
        published_on: datetime field
    """

    name = models.CharField(max_length=200)
    published_on = models.DateTimeField("Published datetime")

    def __str__(self):
        return self.name    

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    created_on = models.DateTimeField('Creation Date Time')

    def __str__(self):
        return self.question_text

    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    created_on = models.DateTimeField('creation datetime')

    def __str__(self):
        return self.choice_text


class YesNoChoices(models.Model):
    YES = 'Yes'
    NO = 'No'
    NONE = 'None'

    CHOICES = [
        (YES, 'yes'),
        (NO, 'no'),
        (NONE, 'None'),
    ]

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    client_choices = models.CharField(max_length=4, choices=CHOICES, default=None)

    def __str__(self):
        return self.client_choices
    
