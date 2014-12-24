from django.shortcuts import render_to_response
from django.views.generic import View
from core.models import Question

class HomeView(View):
    def get(self, request):
        return render_to_response('game/new.html')

class GameView(View):
    def get(self, request):

        question = Question.objects.all().order_by('?')[0]

        return render_to_response('game/game.html', { 'question' : question })
