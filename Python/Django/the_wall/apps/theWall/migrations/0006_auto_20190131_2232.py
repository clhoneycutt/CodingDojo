# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-01 03:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theWall', '0005_auto_20190131_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='userid',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='userid',
            new_name='user',
        ),
    ]