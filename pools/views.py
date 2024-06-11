from django.http import HttpResponse
from django.template import loader

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
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
