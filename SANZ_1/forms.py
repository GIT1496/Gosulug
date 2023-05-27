from django import forms
from .models import SEZ1, LIC1, RESH1
from .models import SEZItem
from .models import SEZSummary

import re
from django.core.exceptions import ValidationError

g = (
    ('Гигиена детей и подростков', 'Гигиена детей и подростков'),
    ('Гигиена труда', 'Гигиена труда'),
    ('Эпид. отдел', 'Эпид. отдел'),
    ('Отдел санитарно-эпидемиологических заключений',
     'Отдел санитарно-эпидемиологических заключений'),
)

class SEZCreateForm(forms.ModelForm):
    class Meta:
        model = SEZ1
        fields = ['Nomer', 'tipogr',"date_creation",'vidano','sootv','deistv']

        widgets = {
            'Nomer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер СЭЗ'
                }
            ),
            'tipogr': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Типографский номер бланка'
                }
            ),
            'date_creation': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'vidano': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Кем выдано',
                }
            ),
            'sootv': forms.CheckboxSelectMultiple( attrs={

                    'placeholder': 'Соответствует СанПин: ',
                }),
            'deistv': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

class LICCreateForm(forms.ModelForm):
    class Meta:
        model = LIC1
        fields = ['Nomer', "date_creation",'INN','OGRN', 'licenz','UR','mesto','vid']

        widgets = {
            'Nomer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер СЭЗ'
                }
            ),
            'licenz': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Наименование лицензиата'
                }
            ),
            'date_creation': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'INN': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ИНН'
                }
            ),
            'OGRN': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ОГРН',
                }
            ),

            'UR': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Юридический адрес лицензиата',
                }
            ),

            'mesto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Место осуществления деятельности',
                }
            ),
            'vid': forms.Select()
        }

class RESHCreateForm(forms.ModelForm):
    class Meta:
        model = RESH1
        fields = ['namber', "date_creation", 'applic','photo']

        widgets = {
            'namber': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер СЭЗ'
                }
            ),
            'applic': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Заявитель (представитель заявителя)'
                }
            ),
            'date_creation': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'photo': forms.FileInput(attrs={'class':'form-control'})

        }


class SEZStatusForm(forms.ModelForm):
    class Meta:
        model = SEZItem
        fields = ['SEZ']

        widgets = {
            'SEZ': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Услуга оказана'
                }
            ),
        }