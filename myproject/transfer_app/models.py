# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models


class TransactionModel(models.Model):
    date = models.DateTimeField(editable=False)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    sender_name = models.CharField(max_length=50)
    sender_phone = models.CharField(max_length=15)
    receiver_name = models.CharField(max_length=50)
    receiver_location = models.CharField(max_length=50)
    receiver_phone = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10)

    def __str__(self):
        return(self.receiver_name)

    def save(self):
        if not self.id:
            self.date = datetime.date.today()
        super(TransactionModel, self).save()
