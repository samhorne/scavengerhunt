from django import forms

class CodeForm(forms.Form):
    code = forms.CharField(label='', max_length=100)