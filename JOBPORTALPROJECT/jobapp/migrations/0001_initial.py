# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-04-30 16:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('degree', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=40)),
                ('resume', models.FileField(default=0, upload_to='resume_files')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(max_length=20)),
                ('cemail', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_apply', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CityJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('company', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
