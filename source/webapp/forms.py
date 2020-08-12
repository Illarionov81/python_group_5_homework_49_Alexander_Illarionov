from django import forms
from django.core.exceptions import ValidationError


from django.forms import widgets

from webapp.models import IssueTracker, Status, Type
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)


def is_title(string):
    if not string[0].isupper():
        raise ValidationError('Это поле надо заплонять с заглавной буквы')


class TaskForm(forms.ModelForm):
    class Meta:
        model = IssueTracker
        fields = ['summary', 'description', 'status', 'type']


# class TaskForm(forms.Form):
#     summary = forms.CharField(max_length=300, required=True, label='Задание', validators=(is_title,))
#     description = forms.CharField(max_length=3500, required=False, initial="None description",
#                                   label='Описание', widget=forms.Textarea, validators=(MinLengthValidator(10),))
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), empty_label='New', label='Status')
#     type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(),  label='Type', widget=widgets.CheckboxSelectMultiple)



    def clean(self):
        cleaned_data = super().clean()
        errors = []
        summary = cleaned_data.get('summary')
        description = cleaned_data.get('description')
        if summary and description and summary == description:
            errors.append(ValidationError("Text of the Summary should not duplicate  Description!"))
        if errors:
            raise ValidationError(errors)
        return cleaned_data