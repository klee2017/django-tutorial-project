from datetime import timedelta

from django.db import models
from django.utils import timezone

class Question(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'설문조사 ({self.title})'

    @property
    def is_recently(self):
        published_date = self.published_date
        if published_date == None:
            return False
        td = timezone.now - self.published_date
        return td < timedelta(days=7)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} (설문: {self.question.title})'
