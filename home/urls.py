from django.urls import path
from . import views

urlpatterns = [
    path('', views.tipousuario, name="usertype"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('signupadmin/', views.create_superuser, name="signupadmin"),
    path('home/', views.inicio, name="inicio"),
    path('avaliacaogeral/', views.avaliacaogeral, name="avaliacaogeral"),
    path('personuser/', views.home, name="personuser"),
    path('projetos/', views.new_project, name="projetos"),
    path('meus_projetos/', views.meus_projetos, name="meus_projetos"),
    path('ranking/', views.ranking, name="ranking"),
    path('search/', views.search, name="search"),
    path('edit_personuser/', views.editar_perfil, name="edit_personuser"),
    path('perfil/', views.home, name="perfil"),  # Rota para o perfil do usuário logado
    path('perfil/<int:user_id>/', views.home, name="perfil_usuario"),  # Rota para o perfil de um usuário específico
    path('usertype/', views.tipousuario, name="tipousuario"),
    path('anotações/', views.anotacao, name="anotar"),
    path('anotacoes/delete/<int:id>/', views.deletar_anotacao, name='deletar_anotacao'),
    path('anotacoes/edit/<int:id>/', views.editar_anotacao, name='editar_anotacao'),
]