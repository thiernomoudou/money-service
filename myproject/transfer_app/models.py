# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TransactionModel(models.Model):
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    sender_name = models.CharField(max_length=50)
    sender_phone = models.CharField(max_length=15)
    receiver_name = models.CharField(max_length=50)
    receiver_location = models.CharField(max_length=50)
    receiver_phone = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10)
