from django.conf.urls import patterns, include, url
from django.shortcuts import render_to_response

from django.views.generic.base import TemplateView

from .views import AddQuestionView

urlpatterns = patterns('',
    url(r'^new/$', AddQuestionView.as_view(), name='new_question'),
    #url(r"^account/", include("account.urls")),
)
