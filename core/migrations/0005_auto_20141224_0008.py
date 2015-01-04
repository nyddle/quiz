# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20141223_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pic',
            field=models.ImageField(upload_to='pics', blank=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/nyddle/quiz/media')),
            preserve_default=True,
        ),
    ]
