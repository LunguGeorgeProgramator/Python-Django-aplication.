from django import forms
from .models import GuideSteps


class IndexFrom(forms.Form):
    # desc = forms.CharField(required=False)
    desc = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder': 'Add guide name ...'
        }
    ))
    # id = forms.HiddenInput()


class DetailsFrom(forms.Form):
    # desc = forms.CharField(required=False)
    id = forms.IntegerField(widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder': 'Add step id ...'
        }
    ))
    step_content = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder':  'Add step content ...'
        }
    ))
    step_selector = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder':  'Add step selector ...'
        }
    ))
    step_next = forms.IntegerField(widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder':  'Add step next ...'
        }
    ))