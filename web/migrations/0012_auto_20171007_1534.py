# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 15:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20171007_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opt',
            name='value',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Category'),
        ),
    ]