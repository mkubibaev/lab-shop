from django import forms
from django.forms import widgets

from webapp.models import CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    description = forms.CharField(max_length=2000, label='Description', widget=widgets.Textarea)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Category', required=True)
    amount = forms.IntegerField(label='Amount', min_value=0, required=True)
    price = forms.DecimalField(max_digits=6, decimal_places=2, label='Price', required=True)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=120, required=False)
