import datetime

from django.db.models import Model
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import IntegerField
from django.db.models import ForeignKey
from django.db.models import CASCADE

from django.utils import timezone


class Question(Model):
	question_text = CharField(max_length=20)
	pub_date = DateTimeField("date published")

	def __str__(self):
		return f"Question(id:{self.id})"

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(Model):
	question = ForeignKey(Question, on_delete=CASCADE)
	choice_text = CharField(max_length=200)
	votes = IntegerField(default=0)

	def __str__(self):
		return f"Choice(id:{self.id})"
