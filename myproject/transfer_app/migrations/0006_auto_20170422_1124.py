# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer_app', '0005_auto_20170418_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='currency',
            field=models.CharField(choices=[('USD', 'Dollar'), ('GNF', 'Francs GN')], max_length=10),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='destination',
            field=models.CharField(choices=[('ANG', 'Angola'), ('GUI', 'Guinea')], max_length=50),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='origin',
            field=models.CharField(choices=[('ANG', 'Angola'), ('GUI', 'Guinea')], max_length=50),
        ),
    ]
