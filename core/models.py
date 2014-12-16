from django.db import models

class Question(models.model):
    name = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
