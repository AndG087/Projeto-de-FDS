from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = "inicio") ,
    path('login/', views.login, name = "login") ,
    path('signup/', views.signup, name = "signup"),
    path('avaliacaogeral/', views.avaliacaogeral, name = "avaliacaogeral"),
    path('personuser/', views.home, name ="personuser"),
    path('projetos/', views.new_project, name ="projetos"),
    path('meus_projetos/', views.meus_projetos, name ="meus_projetos"),
    path('ranking/', views.ranking, name ="ranking"),
    path('search/', views.search, name ="search"),
    
]