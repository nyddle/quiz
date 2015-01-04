# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20141223_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pic',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/Users/nyddle/quiz/media'), blank=True, null=True, upload_to='pics'),
            preserve_default=True,
        ),
    ]
