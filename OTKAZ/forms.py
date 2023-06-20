from django import forms
from .models import OTK, Reestr_1
from .models import OTKItem

import re
from django.core.exceptions import ValidationError

"""Форма для внесения данных в модель отказов"""

class OTKCreateForm(forms.ModelForm):
    class Meta:
        model = OTK
        fields = ['Nomer1', 'prich', "date_creation", 'vidano']
        widgets = {
            'Nomer1': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер письма'
                }
            ),
            'prich': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Причина отказа'
                }
            ),
            'date_creation': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'vidano': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Кем выдано',
                }
            ),

        }

class OTKStatusForm(forms.ModelForm):
    class Meta:
        model = OTKItem
        fields = ['otk']

        widgets = {
            'otk': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Услуга оказана'
                }
            ),
        }