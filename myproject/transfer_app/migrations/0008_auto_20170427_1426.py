# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer_app', '0007_auto_20170422_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='purpose',
            field=models.CharField(choices=[('CASH', 'Cash orange money'), ('PHONE CREDIT', 'Phone Credit')], max_length=50),
        ),
    ]
