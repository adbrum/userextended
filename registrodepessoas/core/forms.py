from django import forms
from registrodepessoas.core.models import Pessoa

CHOICES = (('1', 'Cliente',), ('2', 'Fornecedor',), ('3', 'cliente/fornecedor',), ('4', 'Usuário',))


class LoginForm(forms.Form):
    username = forms.CharField(label="Nome usuário", max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control input-lg'}))
    password = forms.CharField(label="Senha", max_length=32, widget=forms.PasswordInput(
        attrs={'class': 'form-control input-lg'}))
    first_name = forms.CharField(label="Primeiro nome", max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control input-lg'}))
    last_name = forms.CharField(label="Sobrenome", max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control input-lg'}))
    email = forms.EmailField(max_length=32, widget=forms.EmailInput(
        attrs={'class': 'form-control input-lg'}))
    cpf = forms.CharField(label="CPF", max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control input-lg'}))
    rg = forms.CharField(label="RG", max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control input-lg'}))
    choice_field = forms.ChoiceField(widget=forms.Select(attrs={'class': 'selector form-control input-lg'}), choices=CHOICES)
