# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RATapp', '0006_auto_20170322_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default='', max_length=255, verbose_name='firstname'),
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='', max_length=255, verbose_name='lastname'),
        ),
    ]