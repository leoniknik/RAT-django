# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RATapp', '0017_auto_20170325_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crashdescription',
            name='code',
            field=models.CharField(default='', max_length=24, unique=True, verbose_name='code'),
        ),
    ]