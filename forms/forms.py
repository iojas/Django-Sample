from django import forms

class submitURL(forms.Form):
    url = forms.CharField(label='Submit URL')