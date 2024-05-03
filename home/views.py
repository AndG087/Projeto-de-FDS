from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Avaliacao
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from rolepermissions.permissions import revoke_permission
from .models import person
from .models import Projeto
from django.db.models import Count, Avg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as logind
from django.http import HttpResponse
from .models import Avaliacao, Projeto, person



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

            return redirect('inicio')
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

        return redirect('login')
    



def avaliacaogeral(request):
    if request.method == 'POST':
        funcionario_nome = request.POST.get('funcionario_name')
        nota = float(request.POST.get('rate'))
        user_id = request.POST.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            avaliacao = Avaliacao(funcionario_nome=funcionario_nome, nota=nota, user=user)
            avaliacao.save()
            return HttpResponse('avaliacao_sucesso')
        except User.DoesNotExist:
            return HttpResponse('Usuário não encontrado')
    
    # Obtendo todas as avaliações do banco de dados
    avaliacoes = Avaliacao.objects.filter(user=request.user)
    usuarios = User.objects.all()
    
    # Passando as avaliações para o template
    return render(request, 'avaliacaogeral.html', {'avaliacoes': avaliacoes,'usuarios': usuarios})





def home(request):
    if request.method == "GET":
        # Filtrar os projetos onde o usuário atual está listado como participante
        trabalhos = Projeto.objects.filter(participants__icontains=request.user.username)
        contexto = {
            'trabalhos':trabalhos,
            'user':request.user,
        }
        return render(request, "personuser.html", contexto)
    elif request.method == "POST":
        # Aqui você pode processar o envio de arquivos, se necessário
        file = request.POST.get("my_file")
        descricao = request.POST.get("texto")
        
        mf = person(title="minha_imagem", arq=file,descricao=descricao)
        mf.save()
        
        print(file)
        
        return HttpResponse('Foto e informação enviada com sucesso!')
    


    
def new_project(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        participants = request.POST.get('participants')
        usuario = request.user
        
        project = Projeto(name=name, description=description, participants=participants,usuario=usuario)
        project.save()
        return HttpResponse('Projeto criado com sucesso!') 
    else:
        return render(request, 'projetos.html')


def meus_projetos(request):
    return render(request,'meus_projetos.html')


@login_required(login_url="/login/")
def search(request):
    context = {}
    search_term = request.GET.get('search')
    if search_term:
        # Realiza a busca de usuários e projetos com base no termo de pesquisa
        users = User.objects.filter(username__icontains=search_term)
        projects = Projeto.objects.filter(name__icontains=search_term)
        context['users'] = users
        context['projects'] = projects


    return render(request, 'search.html', context)





def ranking(request):
    # Obtendo todos os usuários e suas respectivas avaliações
    usuarios = User.objects.annotate(num_avaliacoes=Count('avaliacao'))

    # Calculando a média das notas recebidas por cada usuário e o total de avaliações feitas daquela pessoa
    for usuario in usuarios:
        avaliacoes_usuario = Avaliacao.objects.filter(funcionario_nome=usuario.username)
        usuario.num_avaliacoes = avaliacoes_usuario.count()  # Contagem das avaliações recebidas
        media = avaliacoes_usuario.aggregate(avg_nota=Avg('nota'))['avg_nota']
        usuario.avg_nota = round(media, 1) if media is not None else None

    # Ordenando os usuários pela média das avaliações em ordem decrescente
    usuarios = sorted(usuarios, key=lambda x: x.avg_nota if x.avg_nota is not None else float('-inf'), reverse=True)

    # Passando os usuários e suas informações para o template
    return render(request, 'ranking.html', {'usuarios': usuarios})
