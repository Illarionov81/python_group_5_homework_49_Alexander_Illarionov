from django import forms
from django.forms import widgets
from webapp.models import IssueTracker, Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'starts_date', 'finish_date']
        widgets = {
                    'starts_date': forms.widgets.SelectDateWidget,
                    'finish_date': forms.widgets.SelectDateWidget,
                   }


class TaskForm(forms.ModelForm):
    class Meta:
        model = IssueTracker
        fields = ['summary', 'description', 'status', 'type']
        widgets = {"type": widgets.CheckboxSelectMultiple}


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


    # def clean(self):
    #     cleaned_data = super().clean()
    #     errors = []
    #     summary = cleaned_data.get('summary')
    #     description = cleaned_data.get('description')
    #     if summary and description and summary == description:
    #         errors.append(ValidationError("Text of the Summary should not duplicate  Description!"))
    #     if errors:
    #         raise ValidationError(errors)
    #     return cleaned_data