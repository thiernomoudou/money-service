from django import forms
from .models import TransactionModel, ReportingModel




class TransactionForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['origin', 'destination', 'sender_name', 'sender_phone', 'receiver_name', 'receiver_location', 'receiver_phone', 'amount', 'currency', 'purpose']
        widgets = {
            'origin': forms.Select(attrs={'class': 'form-control form-element'}),
            'destination': forms.Select(attrs={'class': 'form-control form-element'}),
            'sender_name': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'sender_phone': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'receiver_name': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'receiver_location': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'receiver_phone': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'receiver_location': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'receiver_phone': forms.TextInput(attrs={'class': 'form-control form-element'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control form-element'}),
            'currency': forms.Select(attrs={'class': 'form-control form-element'}),
            'purpose': forms.Select(attrs={'class': 'form-control form-element'})
        }

        


class ReportingForm(forms.ModelForm):
    class Meta:
        model = ReportingModel
        fields = ['origin', 'destination', 'sender_name', 'sender_phone', 'receiver_name', 'receiver_location', 'receiver_phone', 'amount', 'currency', 'purpose']
