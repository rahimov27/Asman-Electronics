from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import CharField
from .models import *

class ClientForms(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'surname', 'phone')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Имя",
            }),
            'surname': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Фамилия",
             }),
            'phone': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Телефон",
            }),
        }