import datetime as dt

from django.core.exceptions import ValidationError


def validate_year(value):
    year = dt.date.today().year
    if value > year:
        raise ValidationError(
            'Год выпуска не может быть больше текущего.'
        )
    if value < 0:
        raise ValidationError(
            'Год выпуска не может быть отрицательным.'
        )
    return value
