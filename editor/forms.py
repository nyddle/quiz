from django.db import models
from django import forms
from django.forms import ModelForm

from core.models import Question

class AddQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = [ 'question', 'pic', 'answer', 'a', 'b', 'c', 'notes', 'published' ]

