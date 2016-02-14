from django import forms
from registrodepessoas.core.models import Pessoa

CHOICES = (('1', 'Cliente',), ('2', 'Fornecedor',), ('3', 'Usuário',))


class LoginForm(forms.Form):
    username = forms.CharField(label="Nome usuário", max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label="Senha", max_length=32, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Primeiro nome", max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Sobrenome", max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=32, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    cpf = forms.CharField(label="CPF", max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    rg = forms.CharField(label="RG", max_length=32, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    choice_field = forms.ChoiceField(widget=forms.Select(attrs={'class': 'selector'}), choices=CHOICES)
