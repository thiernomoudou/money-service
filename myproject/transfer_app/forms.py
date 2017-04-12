from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class TransactionForm(forms.Form):
    pass