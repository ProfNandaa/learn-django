from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
	latest_questions = Question.objects.order_by('-pub_date')[:5]
	data = {
		'latest_questions': latest_questions,
	}
	return render(request, 'polls/index.html', data)

def detail(request, question_id):
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")

	#shortcut
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	response = "You're looking at the results of question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s" % question_id)

# def _render(request, temp, data):
# 	context = RequestContext(request, data)
# 	template = loader.get_template(temp)
# 	return HttpResponse(template.render(context))