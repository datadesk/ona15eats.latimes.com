# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nerd',
            name='twitter_handle',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='yelp_url',
        ),
    ]
