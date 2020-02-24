from .models import Question, Choice
from django.views.generic import ListView, DetailView
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib import messages


class HomeView(ListView):
    model = Question
    template_name = 'polls/index.html'
    ordering = '-pub_date'


class QuestionView(DetailView):
    model = Question
    fields = ['choice_text']
    template_name = 'polls/detail.html'


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, q_id):
    if request.method == 'POST':
        if request.POST.get('choice', False):
            c = Choice.objects.get(pk=request.POST['choice'])
            c.votes += 1
            c.save()
            messages.success(request, "Vote added.")
        else:
            messages.warning(request, "You didn't select a choice.")
    return HttpResponseRedirect(reverse('polls:results', args=(q_id,)))
