# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum, Avg, Max, Min, Count

from .models import TransactionModel, ReportingModel
from .forms import TransactionForm, ReportingForm
import datetime


def index(request):
    if request.user.is_authenticated():
        return home(request)
    else:
        return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def transactions(request):
    form = TransactionForm()
    forms = ReportingForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        forms = ReportingForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('home')
    else:
        return render(request, 'transactions.html', {'form': form})
    

@login_required
def operations(request):
    transactions = TransactionModel.objects.all()
    
    return render(request, 'operations.html', {'transactions':transactions})

@login_required
def reporting(request):
     reports = ReportingModel.objects.all()
            
     return render(request, 'reporting.html', {"reports": reports})

@login_required
def delete(request):
    pk = request.POST.get('pk', 'None')    
    action = get_object_or_404(TransactionModel, pk=pk)
    paction = get_object_or_404(TransactionModel, pk=pk)
    reportaction = ReportingModel()
    model_dic = paction.__dict__
    model_dic.pop(pk, None)
    reportaction.__dict__ = model_dic
    reportaction.pk = None
    reportaction.save()

    action.delete()
    return HttpResponse('')
        
    
@login_required
def summary(request):
    dollar_count = ReportingModel.objects.filter(currency__iexact='usd').count()
    dollar_sum = ReportingModel.objects.filter(currency__iexact='usd').aggregate(Sum('amount')).values()[0]
    gnf_count = ReportingModel.objects.filter(currency__iexact='gnf').count()
    gnf_sum = ReportingModel.objects.filter(currency__iexact='gnf').aggregate(Sum('amount')).values()[0]
    total_processed_count = ReportingModel.objects.count()
    total_pending_count = TransactionModel.objects.count()

    context={'dollar_count': dollar_count, 'dollar_sum': dollar_sum, 'gnf_count': gnf_count, 'gnf_sum': gnf_sum,
        'total_processed_count': total_processed_count, 'total_pending_count': total_pending_count}

    return render(request, 'summary.html', context)