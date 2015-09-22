# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eats', '0003_auto_20150921_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ('distance',)},
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lng',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
