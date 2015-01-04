# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20141222_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pic',
            field=models.ImageField(null=True, blank=True, upload_to='pics'),
            preserve_default=True,
        ),
    ]
