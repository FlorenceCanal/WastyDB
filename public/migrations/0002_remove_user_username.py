# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-12-20 22:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
