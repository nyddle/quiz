from random import shuffle

from django import forms

class QuestionForm(forms.Form):

    question_id = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        self._question = kwargs.pop('question')
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['question_id'].initial = self._question.id
        letters = ('a', 'b', 'c', 'd')
        answers = [self._question.a, self._question.b, self._question.c, self._question.answer]
        shuffle(answers)
        CHOICES = [(letters[i], answers[i]) for i in range(4)]
        self.fields['answer'] = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())


