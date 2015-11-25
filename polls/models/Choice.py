from django.db import models

from .Question import Question

class Choice(models.Model):
    class Meta:
        app_label = 'polls'
        
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text