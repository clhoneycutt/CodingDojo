# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-21 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='note',
            field=models.TextField(default=''),
        ),
    ]
