from django.shortcuts import render
from .models import Question, Choice
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'polls/home.html'

