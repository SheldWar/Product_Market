from django import forms
from django.core import validators


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1, widget=forms.TextInput())
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
