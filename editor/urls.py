from django.conf.urls import patterns, include, url
from django.shortcuts import render_to_response

from django.views.generic.base import TemplateView

from .views import AddQuestionView, QuestionListView, DeleteQuestionView, QuestionView

urlpatterns = patterns('',
    url(r'^new/$', AddQuestionView.as_view(), name='new_question'),
    url(r'^question/(?P<pk>[\w]+)/$', QuestionView.as_view(), name='view_question'),
    url(r'^delete/(?P<pk>[\w]+)/$', DeleteQuestionView.as_view(), name='delete_question'),
    url(r'^edit/(?P<pk>[\w]+)/$', DeleteQuestionView.as_view(), name='edit_question'),
    url(r'^', QuestionListView.as_view(), name='question_list'),
    #url(r"^account/", include("account.urls")),
)
