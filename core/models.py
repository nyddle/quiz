from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User

class Question(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    created = models.DateTimeField('creation date', auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

