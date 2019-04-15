# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
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
header = "<h2> Clique na sua jogada </h2>"


def index(request):
    template = loader.get_template('main.html')
    if 'pedra' in request.POST:
        jog1 = "pedra"
        jog2 = random.choice(jogadas)
        header = "<h2> Você jogou "+jog1
        header += "<br>CP jogou "+jog2
        header += "<br>"+plays[(jog1, jog2)]+"</h2>"
        context = {'header': header}
        return HttpResponse(template.render(context, request))

    if 'papel' in request.POST:
        jog1 = "papel"
        jog2 = random.choice(jogadas)
        header = "<h2> Você jogou "+jog1
        header += "<br>CP jogou "+jog2
        context = {'header': header}
        header += "<br>"+plays[(jog1, jog2)]+"</h2>"
        return HttpResponse(template.render(context, request))

    if 'tesoura' in request.POST:
        jog1 = "tesoura"
        jog2 = random.choice(jogadas)
        header = "<h2> Você jogou "+jog1
        header += "<br>CP jogou "+jog2
        header += "<br>"+plays[(jog1, jog2)]+"</h2>"
        context = {'header': header}
        return HttpResponse(template.render(context, request))

    else:
        header = "<h2>Faça a sua jogada</h2>"
        import pdb
        pdb.set_trace()
        return HttpResponse(template.render(
            context={'header': header},
            request=request)
        )


def login(request):
    template = loader.get_template('login.html')
    if request.method == 'POST':
        user = UserForm(request.POST)
        context = {'user': user}
        if user.is_valid():
            aux = User.objects.get(usuario=user.usuario)
            if(aux.senha == user.senha):
                return HttpResponse(template.render(context, request))
    else:
        user = UserForm()
    context = {'user': user}
    return HttpResponse(template.render(context, request))
# Create your views here.
