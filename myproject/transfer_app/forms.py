from django import forms
from .models import TransactionModel, ReportingModel


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class TransactionForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['origin', 'destination', 'sender_name', 'sender_phone', 'receiver_name', 'receiver_location', 'receiver_phone', 'amount', 'currency', 'purpose']



class ReportingForm(forms.ModelForm):
    class Meta:
        model = ReportingModel
        fields = ['origin', 'destination', 'sender_name', 'sender_phone', 'receiver_name', 'receiver_location', 'receiver_phone', 'amount', 'currency', 'purpose']
