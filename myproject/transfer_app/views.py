# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import TransactionModel, ReportingModel
from .forms import LoginForm, TransactionForm, ReportingForm
import datetime


@login_required
def home(request):
    return render(request, 'home.html')

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    print("the account has been disabled")
            else:
                return HttpResponse("username or password were incorrect")

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def transactions(request):
    form = TransactionForm()
    forms = ReportingForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        forms = ReportingForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            #forms.save(commit=True)
        return redirect('operations')
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
        
    
