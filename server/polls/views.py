from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.conf import settings

from .models import Choice, Question, FirstPoll
from scripts.utils import Rtag, load_config
from .forms import MyForm

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

    if request.method=="POST":
      form=MyForm(request.POST)
      if form.is_valid():
         print("success")
      else:
         print("fail")
    form=MyForm()

    if not request.session.session_key:
        request.session.create()

    R_tag = request.session._session_key
    context = {"Rtag": R_tag}
    email, res_email = Rtag("email", R_tag)
    password, res_password = Rtag("password", R_tag)
    address, res_address = Rtag("address", R_tag)

    config = load_config("config.json")

    context = {
        "email": email,
        "passwd": password,
        "address": address,
        "Rtag" : R_tag,
        "form":form,
        "captcha": config["Captcha"]
    }
    if request.method== "GET":
       #koncepcyjnie
        request.session["res_email"] = email
        request.session["res_address"] = address
        request.session["res_password"] = password
        print(request.session.get("res_email"))

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        try:
                res_email = request.session.get('res_email')
                res_address = request.session.get('res_address')
                res_password = request.session.get('res_password')
                try:
                    email_post = request.POST[res_email] 
                    password_post = request.POST[res_password] 
                    address_post = request.POST[res_address] 
                except:
                    print("error")

                model = FirstPoll(email=email_post, password=password_post, address=address_post)
                model.save()
                print("Model saved")
        except:
                print("Not able to save")

    return render(request, 'polls/boot.html', context)

