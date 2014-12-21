from django.shortcuts import render, render_to_response
from django.views.generic import View, FormView, ListView, CreateView, DeleteView, DetailView

from core.models import Question

from .forms import AddQuestionForm

class AddQuestionView(CreateView):

    form_class = AddQuestionForm
    success_url = '/editor/preview/'
    template_name = 'editor/new.html'

class DeleteQuestionView(DeleteView):

    model  = Question
    success_url = '/editor/'
    template_name = 'editor/delete.html'

class QuestionView(DetailView):

    model  = Question
    success_url = '/editor/'
    template_name = 'editor/question_detail.html'



class QuestionListView(ListView):
    model = Question
    queryset = Question.objects.order_by('-created')
    template_name = 'editor/index.html'
