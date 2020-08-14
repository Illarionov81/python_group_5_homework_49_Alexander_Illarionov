from django.core.exceptions import ValidationError


def is_title(string):
    if not string[0].isupper():
        raise ValidationError('Это поле надо заплонять с заглавной буквы')


def is_null(string):
    if str(0) in string:
        raise ValidationError("Null characters are not allowed.")