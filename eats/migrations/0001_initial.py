# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nerd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('image_url', models.CharField(max_length=200, blank=True)),
                ('twitter_handle', models.CharField(max_length=200, blank=True)),
                ('nerd_bio_url', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('description', models.TextField(blank=True)),
                ('distance', models.DecimalField(max_digits=4, decimal_places=1)),
                ('restaurant_url', models.CharField(max_length=200, blank=True)),
                ('photo_url', models.CharField(max_length=200, blank=True)),
                ('yelp_url', models.CharField(max_length=200, blank=True)),
                ('phone_number', models.CharField(max_length=200, blank=True)),
                ('category', models.CharField(default=b'eats', max_length=200, choices=[(b'eats', b'Eats'), (b'bars', b'bars'), (b'extras', b'Extracurricular')])),
                ('nerd', models.ForeignKey(blank=True, to='eats.Nerd', null=True)),
            ],
        ),
    ]
