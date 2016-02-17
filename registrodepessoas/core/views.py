from django.shortcuts import render
from registrodepessoas.core.forms import LoginForm
from registrodepessoas.core.models import Pessoa


def register(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            tableuser = Pessoa.objects.create(username=form.cleaned_data['username'],
                                              first_name=form.cleaned_data['first_name'],
                                              last_name=form.cleaned_data['last_name'],
                                              email=form.cleaned_data['email'],
                                              # password=form.cleaned_data['password'],
                                              cpf=form.cleaned_data['cpf'],
                                              rg=form.cleaned_data['rg'],
                                              tipo_pessoa=form.cleaned_data['choice_field']
                                              )

            # encripta a pwd
            tableuser.set_password(form.cleaned_data['password'])

            tableuser.save()

        return render(request, 'register.html',
                      {'form': form})
    else:
        return render(request, 'register.html',
                      {'form': LoginForm()})
