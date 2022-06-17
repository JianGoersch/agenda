from django.shortcuts import render, redirect
from core.models import Compromisso
from django.shortcuts import render, redirect
from core.models import Compromisso
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

def login_user(request):
     return render(request, 'login.html')

def logout_user(request):
    logout(request) #limpa a sessão
    return redirect('/')

def submit_login(request):
    if request.POST: #metodo post para provar que a request vem de um navegador
        username = request.POST.get('username') #pegando dados do formulário
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
        return redirect('/')



@login_required(login_url='/login/') #arroba identifica que é um decorator
def lista_compromissos(request):
    usuario = request.user
    compromisso = Compromisso.objects.filter(usuario=usuario)
    dados = {'compromissos':compromisso}
    return render(request, 'agenda.html', dados)