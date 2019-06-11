from django import forms


class IndexFrom(forms.Form):
    # desc = forms.CharField(required=False)
    desc = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder': 'Add guide name ...'
        }
    ))
    # id = forms.HiddenInput()