from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as logind
from django.contrib.auth.decorators import login_required
from .models import Avaliacao
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from rolepermissions.permissions import revoke_permission
from .models import MyFile

@login_required(login_url="/login/")
def inicio(request):
    return render(request,'inicio.html')


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(username=nome,password=senha)

        if user:
            logind(request,user)

            return HttpResponse("Autenticado")
        else:
            return HttpResponse("Nome ou senha incorretos")
            
def signup(request):
    if request.method == "GET":
        return render(request,'signup.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(email=email).first()
        
        if user:
            return HttpResponse("essse email e esse nome já estão cadastrados")
        
        user = User.objects.create_user(username=nome,email=email,password=senha)
        user.save()

        return HttpResponse("Dados salvos")
    

def personuser(request):
    return render(request,'personuser.html')


def avaliacaogeral(request):
    if request.method == 'POST':
        funcionario_nome = request.POST.get('funcionario_name')
        nota = int(request.POST.get('rate'))
        try:
            
            user = User.objects.get(username=funcionario_nome)
            avaliacao = Avaliacao(funcionario_nome=funcionario_nome, nota=nota, user=user)
            avaliacao.save()
            return HttpResponse('avaliacao_sucesso')
           
        except User.DoesNotExist:
            
            error_message = "Usuário não encontrado. Por favor, verifique o nome de usuário e tente novamente."
            return HttpResponse('vai fazer sign in filha da ...')
        
    return render(request, 'avaliacaogeral.html')


def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    elif request.method == "POST":
        file = request.FILES.get("my_file")
        
        if file.size > 20000000:
            return HttpResponse('Arquivo muito grande')
        
        mf = MyFile(title="minha_imagem", arq=file)
        mf.save()
        
        print(file)
        
        return HttpResponse('Foto enviada com sucesso!')
    
def meus_projetos (request):
    return render(request,'meus_projetos.html')
    
def projetos(request):
    return render(request,'projetos.html')
    



