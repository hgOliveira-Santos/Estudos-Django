from django.urls import path
from app_estudos_django import views

urlpatterns = [
    # rota - view responsável - nome de referência
    #facebook.com
    # path('', view=views.home, name='home')
    # facebook.com/devaprender
    # path('devaprender/')

    path('', view=views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')

]
