from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Projeto
from django.db.models import Count, Avg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as logind
from django.http import HttpResponse
from .models import Avaliacao3, Projeto, Foto, Descricao, Feedback3, Anotações
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
import datetime
from datetime import date

@login_required(login_url="/login/")
def inicio(request):
    if request.method == 'GET':
        
        usuarios = User.objects.all()
        total_media_avaliacoes = 0
        total_usuarios = usuarios.count()

        for usuario in usuarios:
            avaliacoes_usuario = Avaliacao3.objects.filter(avaliado=usuario.username)
            usuario.num_avaliacoes = avaliacoes_usuario.count()  
            media = avaliacoes_usuario.aggregate(avg_nota=Avg('nota'))['avg_nota']
            usuario.avg_nota = round(media, 1) if media is not None else None
        
            if media is not None:
                total_media_avaliacoes += media
    
        if total_usuarios > 0:
            media_geral_avaliacoes = total_media_avaliacoes / total_usuarios
        else:
            media_geral_avaliacoes = 0

        usuarios = sorted(usuarios, key=lambda x: x.avg_nota if x.avg_nota is not None else float('-inf'), reverse=True)
        
        # Filtrar projetos ativos e expirados
        usuario_logado = request.user
        trabalhos = Projeto.objects.filter(participants__icontains=usuario_logado.username)
        
        trabalhos_ativos = trabalhos.filter(end_date__gte=date.today()).order_by('end_date')
        trabalhos_expirados = trabalhos.filter(end_date__lt=date.today()).order_by('end_date')

        todos_ativos = Projeto.objects.filter(end_date__gte=date.today()).order_by('end_date')
        todos_expirados = Projeto.objects.filter(end_date__lt=date.today()).order_by('end_date')

    
        contexto = {
            'usuarios': usuarios,
            'media_geral_avaliacoes': round(media_geral_avaliacoes, 1) if total_usuarios > 0 else None,
            'trabalhos': trabalhos,
            'projetos_ativos':trabalhos_ativos,
            'projetos_expirados': trabalhos_expirados,
            'todos_ativos':todos_ativos,
            'todos_expirados': todos_expirados,
        }

        return render(request, 'inicio.html', contexto)
    
    if request.method == 'POST':
            email = request.POST.get('email')
            texto = request.POST.get('texto')
            usuario = request.user
            
            feedback = Feedback3(email=email, texto=texto,user=usuario)
            feedback.save()
    
            return render(request, 'inicio.html')
    
#olá
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
            return render(request, 'login.html', {'error': True})
    
        
            
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
    



@login_required(login_url="/login/")
def avaliacaogeral(request):
    if request.method == 'POST':
        avaliado = request.POST.get('avaliado')
        nota = float(request.POST.get('rate'))
        avaliador = request.user.username  # Nome de usuário do usuário logado

        try:
            user = User.objects.get(username=avaliado)
            avaliacao = Avaliacao3(avaliador=avaliador, avaliado=avaliado, nota=nota, user=user)
            avaliacao.save()
            return JsonResponse({'status': 'success'})  # Retorna uma resposta JSON indicando sucesso
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Usuário não encontrado'})  # Retorna uma resposta JSON indicando erro
    
    # Obtendo todas as avaliações do banco de dados em que o usuário logado é o avaliador
    avaliacoes = Avaliacao3.objects.filter(avaliador=request.user.username)
    
    # Obtendo todos os usuários
    usuarios = User.objects.all()
    
    # Passando as avaliações para o template
    return render(request, 'avaliacaogeral.html', {'avaliacoes': avaliacoes, 'usuarios': usuarios})



#Deploy final.
def home(request, user_id=None):
    if user_id:
        # Recupere o usuário com base no ID fornecido ou retorne um erro 404 se não encontrado
        user = get_object_or_404(User, pk=user_id)
        
        # Agora você pode filtrar os projetos, fotos, descrições e avaliações do usuário específico
        trabalhos = Projeto.objects.filter(participants__icontains=user.username)
        foto = Foto.objects.filter(usuario_id=user.id).order_by('-id').first()
        descricao = Descricao.objects.filter(usuario_id=user.id).order_by('-id').first()
        avaliacoes_usuario = Avaliacao3.objects.filter(avaliado=user.username)
        media_avaliacoes = avaliacoes_usuario.aggregate(avg_nota=Avg('nota'))['avg_nota']
        media_avaliacoes = round(media_avaliacoes, 1) if media_avaliacoes is not None else None
        feedbacks = Feedback3.objects.filter(user=user)
    else:
        # Se nenhum ID de usuário fornecido, carregue o perfil do usuário logado
        user = request.user
        trabalhos = Projeto.objects.filter(participants__icontains=request.user.username)
        foto = Foto.objects.filter(usuario_id=request.user.id).order_by('-id').first()
        descricao = Descricao.objects.filter(usuario_id=request.user.id).order_by('-id').first()
        avaliacoes_usuario = Avaliacao3.objects.filter(avaliado=request.user.username)
        media_avaliacoes = avaliacoes_usuario.aggregate(avg_nota=Avg('nota'))['avg_nota']
        media_avaliacoes = round(media_avaliacoes, 1) if media_avaliacoes is not None else None
        feedbacks = Feedback3.objects.filter(user=user)
        
    contexto = {
        'trabalhos': trabalhos,
        'foto': foto,
        'descricao': descricao,
        'user': user,
        'media_avaliacoes': media_avaliacoes,
        'feedbacks': feedbacks,
    }
    
    return render(request, "personuser.html", contexto)
    
#testescreencast2
def editar_perfil(request):
    if request.method == "GET":
        return render(request, "editar_perfil.html")
    
    elif request.method == "POST":

        foto = request.POST.get("foto")
        descricao = request.POST.get("informacoes_usuario")
        usuario = request.user
        
        if not foto and not descricao:
            return redirect('personuser')
        
        elif not foto:
            descricao = Descricao(descricao=descricao,usuario=usuario)
            descricao.save()
            return redirect('personuser')
            
        elif not descricao:
            foto = Foto(arq=foto,usuario=usuario)
            foto.save()
            return redirect('personuser')
         
        
        foto = Foto(arq=foto,usuario=usuario)
        descricao = Descricao(descricao=descricao,usuario=usuario)
        foto.save()
        descricao.save()
        
        return redirect('personuser')
    

@login_required
def new_project(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        participants = request.POST.get('participants')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        usuario = request.user

        # Validar as datas no formato ISO (YYYY-MM-DD)
        try:
            start_date = datetime.date.fromisoformat(start_date)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Data de início inválida. Use o formato YYYY-MM-DD.'})

        try:
            end_date = datetime.date.fromisoformat(end_date)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Data de término inválida. Use o formato YYYY-MM-DD.'})

        project = Projeto(
            name=name,
            description=description,
            participants=participants,
            start_date=start_date,
            end_date=end_date,
            usuario=usuario
        )
        project.save()
        return JsonResponse({'success': True})
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
    usuarios = User.objects.annotate(num_avaliacoes=Count('avaliacao3'))

    # Calculando a média das notas recebidas por cada usuário e o total de avaliações feitas daquela pessoa
    for usuario in usuarios:
        avaliacoes_usuario = Avaliacao3.objects.filter(avaliado=usuario.username)
        usuario.num_avaliacoes = avaliacoes_usuario.count()  # Contagem das avaliações recebidas
        media = avaliacoes_usuario.aggregate(avg_nota=Avg('nota'))['avg_nota']
        usuario.avg_nota = round(media, 1) if media is not None else None

    # Ordenando os usuários pela média das avaliações em ordem decrescente
    usuarios = sorted(usuarios, key=lambda x: x.avg_nota if x.avg_nota is not None else float('-inf'), reverse=True)

    # Passando os usuários e suas informações para o template
    return render(request, 'ranking.html', {'usuarios': usuarios})
      
def pesquisa_resultado(request, user_id=None):
    if user_id:
        # Recupere o usuário com base no ID fornecido ou retorne um erro 404 se não encontrado
        user = get_object_or_404(User, pk=user_id)
        
        # Agora você pode filtrar os projetos, fotos, descrições e avaliações do usuário específico
        trabalhos = Projeto.objects.filter(participants__icontains=user.username)
        foto = Foto.objects.filter(usuario_id=user.id).order_by('-id').first()
        descricao = Descricao.objects.filter(usuario_id=user.id).order_by('-id').first()
        avaliacoes_usuario = Avaliacao3.objects.filter(avaliado=user.username)
        media_avaliacoes = avaliacoes_usuario.aggregate(avg_nota=Avg('nota'))['avg_nota']
        media_avaliacoes = round(media_avaliacoes, 1) if media_avaliacoes is not None else None
    else:
        # Se nenhum ID de usuário fornecido, carregue o perfil do usuário logado
        user = request.user
        trabalhos = Projeto.objects.filter(participants__icontains=request.user.username)
        foto = Foto.objects.filter(usuario_id=request.user.id).order_by('-id').first()
        descricao = Descricao.objects.filter(usuario_id=request.user.id).order_by('-id').first()
        avaliacoes_usuario = Avaliacao3.objects.filter(avaliado=request.user.username)
        media_avaliacoes = avaliacoes_usuario.aggregate(avg_nota=Avg('nota'))['avg_nota']
        media_avaliacoes = round(media_avaliacoes, 1) if media_avaliacoes is not None else None
        
    contexto = {
        'trabalhos': trabalhos,
        'foto': foto,
        'descricao': descricao,
        'user': user,
        'media_avaliacoes': media_avaliacoes,
    }
    
    return render(request, "pesquisaresultado.html", contexto)


def tipousuario(request):
    return render(request,'tipousuario.html')

def anotacao(request):
    if request.method == "GET":
        user = request.user
        anotacao = Anotações.objects.filter(usuario = user)
        foto = Foto.objects.filter(usuario_id=request.user.id).order_by('-id').first()
        contexto = {
        'anotacao': anotacao,
        'foto': foto,
        }
        
        return render(request, "anotacao.html",contexto)
    
    elif request.method == "POST":
        titulo = request.POST.get("titulo")
        anotacao = request.POST.get("anotacao")
        usuario = request.user
        
        anota = Anotações(titulo=titulo,anotar=anotacao,usuario=usuario)
        anota.save()
        
        anot = Anotações.objects.filter(usuario = usuario)
        foto = Foto.objects.filter(usuario_id=request.user.id).order_by('-id').first()
        
        contexto = {
        'anotacao': anot,
        'foto': foto,
    }
      
        return render(request, "anotacao.html",contexto)
    
def deletar_anotacao(request, id):
    anotacao = get_object_or_404(Anotações, id=id, usuario=request.user)
    anotacao.delete()
    anot = Anotações.objects.filter(usuario = request.user)
    foto = Foto.objects.filter(usuario_id=request.user.id).order_by('-id').first()
        
    contexto = {
        'anotacao': anot,
        'foto': foto,
    }
      
    return render(request, "anotacao.html",contexto)
    

def editar_anotacao(request, id):
    anotacao = get_object_or_404(Anotações, id=id, usuario=request.user)
    if request.method == "GET":
        anot = Anotações.objects.filter(usuario = request.user)
        foto = Foto.objects.filter(usuario_id=request.user.id).order_by('-id').first()
        contexto = {
        'anotacao': anot,
        'foto': foto,
        'u_id':id,
        }
        
        return render(request, "editar_anotacao.html",contexto)
    elif request.method == "POST":
        anotacao.anotar = request.POST.get("anotacao")
        anotacao.save()
        anot = Anotações.objects.filter(usuario = request.user)
        foto = Foto.objects.filter(usuario_id=request.user.id).order_by('-id').first()
        
        contexto = {
            'anotacao': anot,
            'foto': foto,
            'u_id':id,
        }
      
        return render(request, "anotacao.html",contexto)
    


def create_superuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')


        if User.objects.filter(username=username).exists():
                messages.error(request, 'O nome de usuário já existe.')
        elif User.objects.filter(email=email).exists():
                messages.error(request, 'O e-mail já está em uso.')
        else:
            user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
            user.is_superuser = True
            user.is_staff = True
            user.save()
            messages.success(request, 'Superusuário criado com sucesso.')
            return redirect('login')  # Redirecione para uma página adequada
    return render(request, 'createadmin.html')
