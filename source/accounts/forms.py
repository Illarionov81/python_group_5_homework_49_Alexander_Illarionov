from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ValidationError
from django.core.validators import ProhibitNullCharactersValidator

from accounts.models import Profile


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    # first_name = forms.CharField(validators=[ProhibitNullCharactersValidator, ])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        field_classes = {'username': UsernameField}

    def clean(self):
        cleaned_data = super().clean()
        errors = []
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name or last_name:
            pass
        else:
            errors.append(ValidationError("One of the fields: (First name) or (Last name), mast be filled!"))
        if errors:
            raise ValidationError(errors)
        return cleaned_data

    # Автоматическое создание профилей
    def save(self, commit=True):
        user = super().save(commit=commit)
        Profile.objects.create(user=user)
        return user
