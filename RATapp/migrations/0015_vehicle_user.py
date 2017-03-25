# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 21:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RATapp', '0014_remove_vehicle_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]