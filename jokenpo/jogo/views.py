# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import UserForm
from django.template import loader
from .models import User
import random


plays = {("pedra", "pedra"): "Empate",
         ("papel", "papel"): "Empate",
         ("tesoura", "tesoura"): "Empate",
         ("pedra", "tesoura"): "Voce ganhou",
         ("papel", "pedra"): "Voce ganhou",
         ("tesoura", "papel"): "Voce ganhou",
         ("pedra", "papel"): "CP ganhou",
         ("papel", "tesoura"): "CP ganhou",
         ("tesoura", "pedra"): "CP ganhou"}
jogadas = ["pedra", "papel", "tesoura"]
header1 = "Clique na sua jogada"
header2 = ""
header3 = ""


def index(request):
    template = loader.get_template('main.html')
    if 'pedra' in request.POST:
        jog1 = "pedra"
        jog2 = random.choice(jogadas)
        header1 = "\nVocê jogou "+jog1
        header2 = "\n>CP jogou "+jog2
        header3 = "\n"+plays[(jog1, jog2)]+"\n"
        context = {'header1': header1,
                   'header2': header2,
                   'header3': header3}
        return HttpResponse(template.render(context, request))

    if 'papel' in request.POST:
        jog1 = "papel"
        jog2 = random.choice(jogadas)
        header1 = "\nVocê jogou "+jog1
        header2 = "\n>CP jogou "+jog2
        header3 = "\n"+plays[(jog1, jog2)]+"\n"
        context = {'header1': header1,
                   'header2': header2,
                   'header3': header3}
        return HttpResponse(template.render(context, request))

    if 'tesoura' in request.POST:
        jog1 = "tesoura"
        jog2 = random.choice(jogadas)
        header1 = "\nVocê jogou "+jog1
        header2 = "\n>CP jogou "+jog2
        header3 = "\n"+plays[(jog1, jog2)]+"\n"
        context = {'header1': header1,
                   'header2': header2,
                   'header3': header3}
        return HttpResponse(template.render(context, request))

    else:
        header1 = "\nFaça a sua jogada\n"
        return HttpResponse(template.render(
            context={'header1': header1},
            request=request)
        )


def login(request):
    template = loader.get_template('login.html')
    if request.method == 'POST':
        user = UserForm(request.POST)
        context = {'user': user,
                   'result': ""}
        print(user)
        if user.is_valid():
            try:
                aux = User.objects.get(usuario=user.cleaned_data['user'])
                if(aux.senha == user.cleaned_data['password']):
                    return redirect('/jogo/index')
                else:
                    result = "Senha incorreta"
                    context = {'user': user,
                               'result': result}
                    return HttpResponse(template.render(context, request))
            except:
                result = "Usuario não existe"
                context = {'user': user,
                           'result': result}
                return HttpResponse(template.render(context, request))

    else:
        user = UserForm()
    context = {'user': user}
    return HttpResponse(template.render(context, request))
# Create your views here.
