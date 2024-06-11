from django.http import HttpResponse
from django.template import loader
from django.http import Http404

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
	try:
		question = Question.objects.get(id=question_id)
	except Question.DoesNotExist:
		raise Http404("Question not found.")

	template = loader.get_template("pools/detail.html")
	context = {
		"question": question
	}
	response_content = template.render(context=context, request=request)
	return HttpResponse(response_content)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
