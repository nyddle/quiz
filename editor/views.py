from django.shortcuts import render, render_to_response
from django.views.generic import View, FormView

from .forms import AddQuestionForm

class AddQuestionView(FormView):

    form_class = AddQuestionForm
    success_url = '/editor/preview/'

    def get(self, request):
        return render(request, 'editor/new.html')

