from django import forms
from .models import Reestr_1, Reestr_2

import re
from django.core.exceptions import ValidationError
from django.forms.fields import DateField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget




class SEZform(forms.ModelForm):
    class Meta:
        model = Reestr_1
        # fields = '__all__' # Использование всех полей (не реком.)
        fields = ['namber', 'vid','date_creation','date_rendering', 'predpr', 'dejat','fact_adr','adres_Applicant','Otd','sp','Prim',]

        widgets = {
            'namber': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingInput',
                    'placeholder': 'Номер заявления'
                }
            ),
            'date_creation': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'date_rendering': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'predpr': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Заявитель',
                }
            ),
            'dejat': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Наименование деятельности',
                }
            ),
            'fact_adr': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Фактический адрес осуществления деятельности',
                }
            ),
            'adres_Applicant': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Юридический адрес заявителя, представителя заявителя',
                }
            ),
            'Otd': forms.Select(
            ),
            'Prim': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Примечание',
                }
            ),
            'vid': forms.Select(
            ),
            'sp': forms.Select(
            ),

        }

    def clean_name(self):
        name = self.cleaned_data['namber']
        if re.match(r'\d', name):
            raise ValidationError('Поле не должно начинаться с буквы')
        return name


class Reshform(forms.ModelForm):
    class Meta:
        model = Reestr_2
        fields = ['namber', 'date_creation', 'date_rendering', 'fact_adr', 'cl', 'Type_application', 'Object',
                  'Applicant',
                  'adres_Applicant',
                  'adres_Applicant', 'Accredited_organization', 'Accreditation_number', 'Name_obj', 'designer', 'adr',
                  'conclusion_number',
                  'name_acr', 'accreditation', 'adr1', 'SEZ1', 'SEZ2']
        widgets = {
        'namber': forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'Номер заявления'
            }
        ),

        'date_creation': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),

        'date_rendering': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),

        'fact_adr': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Фактический адрес осуществления деятельности',
            }
        ),

        'cl': forms.Select(
        ),

        'Type_application': forms.Select(
        ),

        'Object': forms.Select(
        ),

        'Applicant': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Наименование заявителя, представителя заявителя',
            }
        ),

        'adres_Applicant': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Юридический адрес заявителя',
            }
        ),

        'Accredited_organization': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Аккредитованная организация, проводившая исследования',
            }
        ),

        'Accreditation_number': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Номер аттестата аккредитации организации, проводившей исследования',
            }
        ),

        'Name_obj': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Наименование проекта СЗЗ',
            }
        ),

        'designer': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Наименование проектировщика',
            }
        ),

        'adr': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Юридический адрес проектировщика',
            }
        ),

        'name_acr': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Кем выдано экспертное заключение',
                }
        ),

            'conclusion_number': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Номер экспертного заключения',
            }
        ),

        'accreditation': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Номер аттестата аккредитации экспертной организации',
            }
        ),

        'adr1': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Юридический адрес экспертной организации',
            }
        ),

        'SEZ1': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Номер СЭЗ',
            }
        ),

        'SEZ2': forms.Select(
        ),

    }


class SezOkForm(forms.Form):
    Nomer = forms.CharField(
        max_length=50,
        min_length=2,
        strip=True,
        label='Номер санитарно-эпидемиологического заключения')
    tipogr = forms.CharField(
        max_length=150,
        min_length=2,
        strip=True,
        label='Типографский номер бланка',
        initial="Типографский номер бланка",
        widget=forms.Textarea)
    vidano = forms.FloatField(
        min_value=1,
        # step_size=10,
        label='Кем выдано',
        initial=150)

def clean_date(self):
    name = self.cleaned_data['Nomer']
    if re.match(r'\d', name):
        raise forms.ValidationError('Поле не должно начинаться с буквы')
    else:
        return name

# class SezOtkForm(forms.ModelForm):
#     class Meta:
#         model = Reestr_1
#         # fields = '__all__' # Использование всех полей (не реком.)
#         fields = ['Prichina', 'Vip']
#         widgets = {
#             'Prichina': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Причина отказа',
#                 }
#             ),
#             'Vip': forms.RadioSelect(),
#         }

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class LoginForm(AuthenticationForm):
        username = forms.CharField(
            label='Логин',
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        password = forms.CharField(
            label='Пароль',
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )






# email
class ContactForm(forms.Form):
    recipient = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    subject = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    content = forms.CharField(
        label='Текст письма',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 8
            }
        )
    )

