# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 11:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_document_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='author',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]