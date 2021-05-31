from django.http import request, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.contrib import messages
from .models import Cliente, User_Credor, Credor



# ---------- GENERAL VIEWS ----------
class HomePageView(LoginRequiredMixin, TemplateView):
    """ View para a página principal. """
    template_name = "webpage/index.html"


class CadastrarCliente(LoginRequiredMixin, TemplateView):
    """ View de cadastro de clientes na base de dados. """
    template_name = "webpage/clientes/cadastrar.html"

    def post(self, request):
        messages.info(request, 'Cliente cadastrado com sucesso!')
        return redirect('cadastro_cliente')

# ---------- Autenticação -----------
def LoginView(request):
    """ View para manipulação do login. """
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate_user(email, password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('index')

        else:
            messages.error(request, 'O usuário não existe ou a senha não corresponde.')
            return redirect('login')

    else:
        return render(request, "webpage/login.html")

@login_required
def Logout(request):
    """ View para manipulação do logout. """
    logout(request)

    messages.info(request, 'Você saiu da sua conta.')
    return redirect('login')
    
# ---------- HELPERS -----------
def authenticate_user(email, password):
    """ Helper para autenticação usando o e-mail """
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user

    return None