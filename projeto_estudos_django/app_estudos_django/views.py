from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuários/home.html')

def usuarios(request):
    #salvando os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.idade = request.POST.get("idade")
    novo_usuario.save()

    #exibir os usuários cadastrados em uma nova página

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #retornar os dados para a página de listagem de usuários

    return render(request, 'usuários/usuarios.html', usuarios)