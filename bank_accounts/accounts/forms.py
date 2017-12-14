from django import forms


class AccountForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    iban = forms.CharField(required=True)
