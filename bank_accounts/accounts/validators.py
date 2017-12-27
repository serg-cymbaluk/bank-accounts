import re

from django.conf import settings
from django.core.validators import BaseValidator, ValidationError
from django.utils.deconstruct import deconstructible

IBAN_COUNTRIES = getattr(settings, 'IBAN_COUNTRIES', [])


@deconstructible
class IBANValidator(BaseValidator):
    """
    Validator for IBAN accounts.
    Checks IBAN structure, length and checksum.
    This validator doesn't check domestic account check digit.
    So some wrong accounts can be mistakenly accepted but not vice versa.
    """
    messages = {
        'checksum': 'Wrong IBAN checksum.',
        'country_code': 'Wrong country code.',
        'length': 'Wrong IBAN length (should be {}).',
        'structure': 'Wrong IBAN structure.',
    }

    def __init__(self):
        pass

    def __call__(self, value):
        match = re.match(r'([A-Z]{2})([0-9]{2}).+', value)
        if not match:
            raise ValidationError(self.messages['structure'])

        country, checksum = match.groups()
        length = dict(IBAN_COUNTRIES).get(country)

        if not length:
            raise ValidationError(self.messages['country_code'])

        if len(value) != length:
            raise ValidationError(self.messages['length'].format(length))

        self.validate_checksum(value)

    def validate_checksum(self, value):
        """
        Validate IBAN checksum using algorithm:
        https://www.alpha.gr/files/personalbanking/iban_check_digit_En.pdf
        """
        check_number = ''
        for symbol in value[4:] + value[:4]:
            check_number += str(ord(symbol) - 55) if symbol.isupper() else symbol

        try:
            check_number = int(check_number)
        except ValueError as e:
            raise ValidationError(self.messages['structure'])

        if check_number % 97 != 1:
            raise ValidationError(self.messages['checksum'])
