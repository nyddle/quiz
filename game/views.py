from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from core.models import Question
from .forms import QuestionForm

class HomeView(View):
    def get(self, request):
        return render_to_response('game/new.html')

class GameView(View):
    def get(self, request):

        question = Question.objects.all().order_by('?')[0]
        form = QuestionForm(question=question)

        return render_to_response('game/game.html', { 'question' : question, 'form' : form }, RequestContext(request))

    def post(self, request):

        question_id = request.POST.get('question_id')
        answer = request.POST.get('answer')

        cquestion = Question.objects.get(id=question_id)

        question = Question.objects.all().order_by('?')[0]
        form = QuestionForm(question=question)

        return render_to_response('game/game.html', { 'question' : question, 'form' : form }, RequestContext(request))
