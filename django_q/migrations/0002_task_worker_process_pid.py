# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-21 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_q', '0001_squashed_0002_auto_20160815_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='worker_process_pid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
