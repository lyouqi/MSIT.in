# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20170121_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestnews',
            name='link',
            field=models.CharField(help_text='Link for the News', max_length=1000),
        ),
    ]