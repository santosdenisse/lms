# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0010_auto_20160111_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='category',
            field=models.CharField(max_length=30),
        ),
    ]
