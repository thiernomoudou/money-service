# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer_app', '0002_transactionmodel_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.CharField(max_length=12)),
            ],
        ),
    ]
