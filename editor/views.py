from django.shortcuts import render, render_to_response
from django.views.generic import View

class AddQuestionView(View):

    def get(self, request):
        return render(request, 'editor/new.html')

