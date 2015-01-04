# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20141224_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='notes',
            field=models.CharField(default=0, max_length=4000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='published',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
