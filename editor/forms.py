from django.db import models
from django import forms
from django.forms import ModelForm

from core.models import Question

class EditQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = [ 'question', 'answer', 'a', 'b', 'c' ]

