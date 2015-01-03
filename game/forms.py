from django import forms

class QuestionForm(forms.Form):

    question_id = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        self._question = kwargs.pop('question')
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['question_id'].initial = self._question.id
        CHOICES=[('A','Answer 1'),
         ('B','Answer 2')]
        self.fields['answer'] = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

"""
CHOICES=[('select1','select 1'),
         ('select2','select 2')]

like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
"""

