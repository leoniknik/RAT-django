# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RATapp', '0029_offer_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='highoffer',
            name='message',
        ),
        migrations.RemoveField(
            model_name='highoffer',
            name='price',
        ),
    ]
