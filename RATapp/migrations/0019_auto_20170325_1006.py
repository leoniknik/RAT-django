# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RATapp', '0018_auto_20170325_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='crash',
            name='date',
            field=models.DateField(null=True, verbose_name='crash_date'),
        ),
    ]