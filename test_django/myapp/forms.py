from cProfile import label
from django import forms

class InputForm(forms.Form):
    data = forms.CharField()