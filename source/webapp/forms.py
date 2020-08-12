from django import forms
from django.core.exceptions import ValidationError

from .models import Status, Type
from django.forms import widgets


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=300, required=True, label='Задание')
    description = forms.CharField(max_length=3500, required=False, initial="None description",
                                  label='Описание', widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), empty_label='New', label='Status')
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(),  label='Type', widget=widgets.CheckboxSelectMultiple)



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