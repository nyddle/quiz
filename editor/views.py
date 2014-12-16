from django.shortcuts import render, render_to_response
from django.views.generic import View

class AddQuestionView(View):

    def get(self, request):
        return render_to_response('editor/new.html')

