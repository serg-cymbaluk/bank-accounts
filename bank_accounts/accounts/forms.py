from django import forms
from django.forms import widgets

from .validators import IBANValidator


class IBANWidget(widgets.MultiWidget):
    """
    Widget for IBAN field.
    Allows input IBAN value using separated 4-digit text inputs.
    """
    template_name = 'accounts/widgets/iban.html'

    def __init__(self, attrs=None):
        iban_widgets = [
            widgets.TextInput() for i in range(9)
        ]

        super().__init__(iban_widgets, attrs=attrs)

    def decompress(self, value):
        if (value):
            return [value[i:i+4] for i in range(0, len(value), 4)]
        return []

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        value = super().value_from_datadict(data, files, name)
        return ''.join(value)


# Form class is more suitable than ModelForm because we manage data from two models.
class AccountForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    iban = forms.CharField(
        required=True,
        validators=[IBANValidator()],
        widget=IBANWidget
    )
