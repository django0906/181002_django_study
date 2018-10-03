from django.db import models
from django.utils import timezone

import datetime


class Question(models.Model):
    '''
    PK를 안만들면 id값을 Django가 만들어 버리는 듯
    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # 이 버그는 수정되어야 한다!
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    '''
    FK로 뒀기 때문에 예제에서의 q변수가 접근가능했음.
    '''
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
