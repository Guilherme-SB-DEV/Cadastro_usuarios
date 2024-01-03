from django.urls import path
from app import views

urlpatterns = [
    #rota responsavel e nome de referencia
    path('',views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios' )
]
