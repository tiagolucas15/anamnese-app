from django.forms import ModelForm, CharField, HiddenInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *
from .choices import *


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'


class AnamneseForm(ModelForm):
    # tipo_exame = forms.CharField(widget=forms.RadioSelect(choices=TIPO_EXAME))

    class Meta:
        model = Anamnese
        fields = '__all__'


class CriarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Medico
        fields = ('crm', 'senha',)


class UploadFichaForm(forms.ModelForm):
    class Meta:
        model = FichaAnamnse
        fields = '__all__'
