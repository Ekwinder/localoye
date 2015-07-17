# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20150717_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
