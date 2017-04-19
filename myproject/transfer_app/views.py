# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import TransactionModel, ReportingModel
from .forms import LoginForm, TransactionForm, ReportingForm
import datetime


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


def transactions(request):
    form = TransactionForm()
    forms = ReportingForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        forms = ReportingForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            forms.save(commit=True)
            # TransactionModel.objects.create(origin=form.cleaned_data['origin'], destination=form.cleaned_data['destination'], sender_name=form.cleaned_data['sender_name'], sender_phone=form.cleaned_data['sender_phone'], receiver_name=form.cleaned_data['receiver_name'], receiver_location=form.cleaned_data['receiver_location'], receiver_phone=form.cleaned_data['receiver_phone'], amount=form.cleaned_data['amount'], currency=form.cleaned_data['currency'] )
        return redirect('operations')
    else:
        return render(request, 'transactions.html', {'form': form})
    

def operations(request):
    transactions = TransactionModel.objects.all()
    
    return render(request, 'operations.html', {'transactions':transactions})

def reporting(request):
     reports = ReportingModel.objects.all()
            
     return render(request, 'reporting.html', {"reports": reports})


def delete(request):
    pk = request.GET.get('pk', 'None')    
    action = get_object_or_404(TransactionModel, pk=pk)
    action.delete()
    return HttpResponse('')
    return redirect('operations')
        
    
