from django.shortcuts import render, redirect
from .models import RegistroAcesso, Visitante
from .forms import EnderecoForm, VeiculoForm, VisitanteForm, RegistroAcessorForm
from django.shortcuts import datetime

# Create your views here.

def index(request):
    acessos = RegistroAcesso.objects.all()
    context = { "acessos": acessos }
    return render

def visitantes(requets):

