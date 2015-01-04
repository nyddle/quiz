# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='pic',
            field=models.ImageField(upload_to='', blank=True, null=True),
            preserve_default=True,
        ),
    ]
