from django import forms
from .models import Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=300, required=True, label='Задание')
    description = forms.CharField(max_length=3500, required=False, initial="None description",
                                  label='Описание', widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), empty_label='New', label='Status')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), empty_label='Bug', label='Type')
