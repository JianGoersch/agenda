from django.shortcuts import render, redirect
from core.models import Compromisso

# Create your views here.

# def lista_compromissos(request):
#     usuario = request.user
#     compromisso = Compromisso.objects.filter(usuario=usuario) #listando por usuário logado no database
#     dados = {'compromissos':compromisso}
#     return render(request, 'agenda.html', dados)
#

#primeiro método para redirecionar a pag inicial

def index(request):
    return redirect('agenda/')

def lista_compromissos(request):
    compromisso = Compromisso.objects.all()
    dados = {'compromissos':compromisso}
    return render(request, 'agenda.html', dados)