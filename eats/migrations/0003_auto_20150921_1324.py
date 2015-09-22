# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eats', '0002_auto_20150921_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='distance',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=1),
        ),
    ]
