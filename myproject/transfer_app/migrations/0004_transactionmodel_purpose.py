# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer_app', '0003_trial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionmodel',
            name='purpose',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
    ]