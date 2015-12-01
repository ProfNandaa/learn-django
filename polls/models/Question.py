from .__shared_imports import *

import datetime
from django.utils import timezone


class Question(models.Model):

    class Meta:
        app_label = 'polls'

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolen = True
    was_published_recently.short_description = 'Published recently?'

    @classmethod
    def get(cls, pk=0):
        if pk > 0:
            return cls.objects.get(pk=pk)
        return cls.objects.all()

