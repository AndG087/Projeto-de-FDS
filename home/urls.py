from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('avaliacaogeral/', views.avaliacaogeral, name="avaliacaogeral"),
    path('personuser/', views.home, name="personuser"),
    path('projetos/', views.new_project, name="projetos"),
    path('meus_projetos/', views.meus_projetos, name="meus_projetos"),
    path('ranking/', views.ranking, name="ranking"),
    path('search/', views.search, name="search"),
    path('edit_personuser/', views.editar_perfil, name="edit_personuser"),
    path('perfil/', views.home, name="perfil"),  # Rota para o perfil do usuário logado
    path('perfil/<int:user_id>/', views.home, name="perfil_usuario"),  # Rota para o perfil de um usuário específico
]