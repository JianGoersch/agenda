from django.shortcuts import render, redirect
from core.models import Compromisso
from django.shortcuts import render, redirect
from core.models import Compromisso
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta #era para o método com 1h de atraso
from django.http.response import Http404, JsonResponse

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
    compromisso = Compromisso.objects.filter(usuario=usuario) #__significa maior que no django/ __lt significa menor que
    dados = {'compromissos':compromisso}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/') #loguin_requeride faz a requisição de estar logado
def compromisso(request):
    id_compromisso = request.GET.get('id')
    dados = {}
    if id_compromisso:
        dados['compromisso'] = Compromisso.objects.get(id=id_compromisso)
    return render(request, 'compromisso.html', dados)

@login_required(login_url='/login/')
def submit_compromisso(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_compromisso = request.POST.get('id_compromisso')
        if id_compromisso: #segunda forma de atualizar
            compromisso = Compromisso.objects.get(id=id_compromisso)
            if compromisso.usuario == usuario:
                compromisso.titulo = titulo
                compromisso.descricao = descricao
                compromisso.data_evento = data_evento
                compromisso.save()
            #Compromisso.objects.filter(id=id_compromisso).update(titulo=titulo, data_evento=data_evento, descricao=descricao) #primeira forma de se fazer uma atualização
        else:
            Compromisso.objects.create(titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario)
        return redirect('/')

@login_required(login_url='/login/')
def delete_compromisso(request, id_compromisso):
    usuario = request.user
    try:
        compromisso = Compromisso.objects.get(id=id_compromisso)
    except Exception:
        raise Http404()
    if usuario == compromisso.usuario: #validação para o user poder excluir apenas compromissos próprios
        compromisso.delete()
    else:
        raise Http404
    return redirect('/')
#metodo para carregar json
@login_required(login_url='/login/')
def json_lista_compromisso(request):
    usuario = request.user
    compromisso = Compromisso.objects.filter(usuario=usuario).values('id', 'titulo')  # __significa maior que no django/ __lt significa menor que
    return JsonResponse(list(compromisso), safe=False)