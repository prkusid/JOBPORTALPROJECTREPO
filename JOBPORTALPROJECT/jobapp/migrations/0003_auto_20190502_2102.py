# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-02 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_auto_20190501_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='designation',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cityjobs',
            name='designation',
            field=models.CharField(max_length=255),
        ),
    ]
