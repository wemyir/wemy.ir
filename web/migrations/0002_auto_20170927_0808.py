# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-27 08:08
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='excerpt',
            field=models.TextField(default='', help_text='\u067e\u06cc\u0634 \u0641\u0631\u0636 \u0645\u0642\u062f\u0627\u0631\u06cc \u0627\u0632 \u0645\u062a\u0646 \u0627\u0635\u0644\u06cc \u06af\u0631\u0641\u062a\u0647 \u0645\u06cc\u0634\u0648\u062f'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='blog/%Y-%m-%d', verbose_name='main image'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='posts',
            name='url',
            field=models.CharField(default='', help_text='(\u067e\u06cc\u0634 \u0641\u0631\u0636 \u0627\u0633\u0644\u0634 \u0639\u0646\u0648\u0627\u0646 \u0645\u0637\u0644\u0628)', max_length=200),
        ),
    ]
