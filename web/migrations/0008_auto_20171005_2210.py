# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20171005_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
