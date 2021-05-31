from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('cliente/cadastro', views.CadastrarCliente.as_view(), name='cadastro_cliente'),
    path('login', views.LoginView, name='login'),
    path('logout', views.Logout, name='logout'),
]