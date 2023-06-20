from django import forms
from .models import Reestr_1, Reestr_2
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


"""Форма для ввода заявления на СЭЗ """

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
            # 'predpr': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Заявитель',
            #         'autocomplete': 'off',
            #     }
            # ),
            'dejat': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Наименование деятельности/Причина переоформления',
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
        predpr = forms.ModelChoiceField(queryset=Reestr_1.objects.all(),
                                      widget=forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Заявитель'}))


"""Форма для ввода заявления на Решение СЗЗ"""
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

# Форма для регистрации

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

# email (форма для обратной связи)
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

