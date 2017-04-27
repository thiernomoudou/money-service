# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
COUNTRY_CHOICES = (
    ('ANGOLA', 'Angola'),
    ('GUINEA', 'Guinea')
    )

CURRENCY_CHOICES = (
    ('USD', 'Dollar'),
    ('GNF', 'Francs GN')
    )

PURPOSE_CHOICES = (
    ('CASH', 'Cash $'),
    ('ORANGE MONEY', 'Orange Money'),
    ('PHONE CREDIT', 'Phone Credit')
    )

class TransactionModel(models.Model):
    date = models.DateTimeField(editable=False)
    origin = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    destination = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    sender_name = models.CharField(max_length=50)
    sender_phone = models.CharField(max_length=15)
    receiver_name = models.CharField(max_length=50)
    receiver_location = models.CharField(max_length=50)
    receiver_phone = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES)

    def __str__(self):
        return(self.receiver_name)

    def save(self):
        if not self.pk:
            self.date = datetime.date.today()
        super(TransactionModel, self).save()


class ReportingModel(models.Model):
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
    purpose = models.CharField(max_length=50)

    def __str__(self):
        return(self.receiver_name)

    def save(self):
        if not self.pk:
            self.date = datetime.date.today()
        super(ReportingModel, self).save()
