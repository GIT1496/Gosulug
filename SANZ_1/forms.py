from django import forms
from .models import SEZ1, LIC1, RESH1, SVID, Pereoformlen
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
        fields = ['Nomer', "date_creation", 'vid']

        widgets = {
            'Nomer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер СЭЗ'
                }
            ),

            'date_creation': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),

            'vid': forms.Select()
        }

class RESHCreateForm(forms.ModelForm):
    class Meta:
        model = RESH1
        fields = ['namber', "date_creation", 'applic','kl', 'photo']

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
            'kl': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Класс опасности'
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

class SVIDCreateForm(forms.ModelForm):
    class Meta:
        model = SVID
        fields = ['Nomer', "date_creation", 'tipogr', 'obl', 'Svid_vid', 'firm', 'Norm']

        widgets = {
            'Nomer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер Свидетельства о государственной регистрации'
                }
            ),
            'date_creation': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'tipogr': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Типографский номер бланка'
                }
            ),
            'Svid_vid': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Свидетельство выдано на основании'
                }
            ),
            'obl': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Типографский номер бланка'
                }
            ),
            'firm': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Фирма заявитель'
                }
        ),
            'Norm': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Нормативная документация'
                }
        ),

        }

class PEREOFCreateForm(forms.ModelForm):
    class Meta:
        model = Pereoformlen
        fields = ['nomer', "nomer2", 'date', 'prich']

        widgets = {
            'nomer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер переоформляемого документа'
                }
            ),
            'nomer2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер нового документа'
                }
            ),
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'prich': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Причина переоформления'
                }
            ),


        }
