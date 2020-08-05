from django import forms
from .models import Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=300, required=True, label='Задание')
    description = forms.CharField(max_length=3500, required=False, initial="None description",
                                  label='Описание', widget=forms.Textarea)


class StatusForm(forms.Form):
    status = forms.ModelChoiceField(queryset=Status.objects.all(),  label='Status')


class TypeForm(forms.Form):
    type = forms.ModelChoiceField(queryset=Type.objects.all(),  label='Type')





