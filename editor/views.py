from django.shortcuts import render, render_to_response
from django.views.generic import View, FormView, ListView

from core.models import Question

from .forms import AddQuestionForm

class AddQuestionView(FormView):

    form_class = AddQuestionForm
    success_url = '/editor/preview/'
    template_name = 'editor/new.html'

#    def get(self, request):
#        return render(request, 'editor/new.html')


class QuestionListView(ListView):
    model = Question
    queryset = Question.objects.order_by('-created')
    template_name = 'editor/index.html'
"""
    def get_queryset(self):
        queryset = super(QuestionListView, self).get_queryset()
        if 'tag' in self.kwargs:
            tag = self.kwargs['tag']
            return queryset.filter(tags__name__in=[tag,])
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(question__icontains=q)
        return queryset
"""
