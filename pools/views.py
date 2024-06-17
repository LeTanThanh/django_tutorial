from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.db.models import F

from .models import Question

def index(request):
	template = loader.get_template("pools/index.html")

	questions = Question.objects.order_by("-pub_date")[:5]
	context = {
		"questions": questions
	}
	response_content = template.render(context=context, request=request)
	return HttpResponse(response_content)

def detail(request, question_id):
	# try:
	# 	question = Question.objects.get(id=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question not found.")
	question = get_object_or_404(Question, id=question_id)

	template = loader.get_template("pools/detail.html")
	context = {
		"question": question
	}
	response_content = template.render(context=context, request=request)
	return HttpResponse(response_content)

def results(request, question_id):
	question = get_object_or_404(Question, id=question_id)
	return render(
     	request=request,
     	template_name="pools/results.html",
      	context={
			"question": question
		})

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

		return HttpResponseRedirect(reverse("pools:question_results", args=(question.id,)))
