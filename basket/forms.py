from django import forms
"""Форма для добавления заявления в сессию"""

PROD_MAX_COUNT = [(i, str(i)) for i in range(1,2)]

class BasketAddProductForm(forms.Form):
    count_prod = forms.TypedChoiceField(choices=PROD_MAX_COUNT, coerce=int, label='Количество:')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)