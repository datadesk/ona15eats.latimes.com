# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eats', '0004_auto_20150921_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='photo_credit',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
