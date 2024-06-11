from django.db.models import Model
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import ForeignKey
from django.db.models import CASCADE

class Question(Model):
  question_text = CharField(max_length=20)
  pub_date = DateTimeField("date published")

class Choice(Model):
  question = ForeignKey(Question, on_delete=CASCADE)
  choice_text = CharField(max_length=200)
  votes = IntegerField(default=0)
