from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader


def inicio(request):
    plantilla = loader.get_template('blogcoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)