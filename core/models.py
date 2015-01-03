import os

#from django.conf import settings

from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class Question(models.Model):
    question = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='pics',blank=True,storage=fs)
    answer = models.CharField(max_length=200)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    created = models.DateTimeField('creation date', auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    published = models.BooleanField(blank=True)
    notes = models.CharField(max_length=4000)
