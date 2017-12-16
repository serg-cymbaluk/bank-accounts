from django import forms


# Form class is more suitable than ModelForm because we manage data from two models.
class AccountForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=150)
    iban = forms.CharField(required=True, max_length=34)
