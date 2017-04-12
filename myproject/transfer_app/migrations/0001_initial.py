# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('sender_name', models.CharField(max_length=50)),
                ('sender_phone', models.CharField(max_length=15)),
                ('receiver_name', models.CharField(max_length=50)),
                ('receiver_location', models.CharField(max_length=50)),
                ('receiver_phone', models.CharField(max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('currency', models.CharField(max_length=10)),
            ],
        ),
    ]
