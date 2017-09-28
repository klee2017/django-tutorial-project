from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateTimeField()

    def __str__(self):
        return print('{}'.format(self.title))

class Choice(models.Model):
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)