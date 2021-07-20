from django.core.exceptions import ValidationError


def is_integer(value):
    if not isinstance(value, int):
        raise ValidationError(
            '%(value)s is not an integer',
            params={'value': value},
        )


def is_positive(value):
    if isinstance(value, float) and value <= 0.0:
        raise ValidationError(
            'input cannot be zero'
        )
    elif isinstance(value, int) and value <= 0:
        raise ValidationError(
            'input cannot be zero'
        )
