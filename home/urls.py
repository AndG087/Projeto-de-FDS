from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = "inicio") ,
    path('login/', views.login, name = "login") ,
    path('signup/', views.signup, name = "signup"),
    path('avaliacaogeral/', views.avaliacaogeral, name = "avaliacaogeral"),
    path('personuser/', views.personuser, name ="personuser"),
    path('projetos/', views.projetos, name ="projetos"),
    path('meus_projetos/', views.meus_projetos, name ="meus_projetos")
]