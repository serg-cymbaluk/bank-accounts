from django import template

register = template.Library()

@register.filter(name='iban')
def format_iban(value):
    """
    Format IBAN value as dash separated string
    Example:
        value = 'UA112222333344445555'
        {{ value | iban }}

        output:
        UA11-2222-3333-4444-5555
    """
    return '-'.join([value[i:i+4] for i in range(0, len(value), 4)])
