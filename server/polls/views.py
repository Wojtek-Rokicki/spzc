from ctypes import addressof
from curses.ascii import HT
import re
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.conf import settings
from django.template import Context

from .models import Choice, Question, FirstPoll
from scripts.utils import Rtag, decrypt


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        print(request.session._session_key)
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def boot(request: HttpRequest):
    # 1.
    # info o sesji - https://docs.djangoproject.com/en/4.0/topics/http/sessions/
    # zapisanie wygenerowanych wartości losowych dla danego użytkownika
    # 2.
    # Zmodyfikowanie renderingu - wstawienie modyfikacji w tagach
    #session_key = request.COOKIES[settings.SESSION_COOKIE_NAME]

    if not request.session.session_key:
        request.session.create()

    R_tag = request.session._session_key
    context = {"Rtag": R_tag}

    email, res_email = Rtag("email", R_tag)
    password, _ = Rtag("password", R_tag)
    address, _= Rtag("address", R_tag)

    context = {
        "email": email,
        "passwd": password,
        "address": address,
        "Rtag" : R_tag
    }

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        try:
            print(request.POST)
            print(email)
            if res_email:
                print(decrypt(res_email))
            email_post = request.POST[email]
            print(email_post)
            password_post = request.POST[password]
            address_post = request.POST[address]
            model = FirstPoll(email=email_post, password=password_post, address=address_post)
            model.save()
            print("Model saved")
        except:
            print("Not able to save")

    return render(request, 'polls/boot.html', context)
