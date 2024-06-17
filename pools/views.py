from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.db.models import F
from django.views import generic

from .models import Question

class IndexView(generic.ListView):
	def get_queryset(self):
		return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question


class ResultView(generic.DetailView):
    model = Question
    template_name = "pools/question_result.html"



def vote(request, question_id):
	question = get_object_or_404(Question, id=question_id)
	try:
		selected_choice = question.choice_set.get(id=request.POST["choice"])
	except ():
		return render(
			request = request,
			template_name = "pools/detail.html",
			context = {
				"question": question,
				"error_message": "You didn't select a choice."
			}
		)
	else:
		selected_choice.votes = F("votes") + 1
		selected_choice.save()

		return HttpResponseRedirect(reverse("pools:question_result", args=(question.id,)))
