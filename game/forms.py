from django import forms

class QuestionForm(forms.Form):

    CHOICES=[('A','select 1'),
         ('B','select 2')]
    answer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    def __init__(self, *args, **kwargs):
        self._question = kwargs.pop('question')
        super(QuestionForm, self).__init__(*args, **kwargs)

"""
CHOICES=[('select1','select 1'),
         ('select2','select 2')]

like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
"""

