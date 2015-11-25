from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models.Choice import Choice
from .models.Question import Question


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

    # shortcut
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def user_register(request):
    # redo with Django forms
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return HttpResponseRedirect(reverse('polls:index'))
    else:
        return render(request, 'polls/register.html', {})


def user_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/polls/user/profile')
            else:
                return HttpResponse("Account has been disabled")
        else:
            error = "Wrong username/password combination"
    return render(request, 'polls/login.html', {'error': error})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/polls/user/login')


@login_required(login_url='/polls/user/login')
def user_profile(request):
    return render(request, 'polls/user_profile.html', {})


def custom_404(request):
    return render(request, 'polls/404.html')

# Django generic views


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        '''Return the last five questions'''
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
