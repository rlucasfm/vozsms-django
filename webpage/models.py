from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Credor(models.Model):
    nome        = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome        = models.CharField(max_length=200)
    cpfcnpj     = models.CharField(max_length=16)
    endereco    = models.CharField(max_length=256, null=True)
    bairro      = models.CharField(max_length=128, null=True)
    cidade      = models.CharField(max_length=128, null=True)
    cep         = models.CharField(max_length=16, null=True)
    uf          = models.CharField(max_length=2, null=True)
    telefone1   = models.CharField(max_length=32, null=True)
    telefone2   = models.CharField(max_length=32, null=True)
    telefone3   = models.CharField(max_length=32, null=True)
    telefone4   = models.CharField(max_length=32, null=True)
    telefone5   = models.CharField(max_length=32, null=True)
    telefone6   = models.CharField(max_length=32, null=True)
    email1      = models.CharField(max_length=200, null=True)
    email2      = models.CharField(max_length=200, null=True)
    email3      = models.CharField(max_length=200, null=True)
    email4      = models.CharField(max_length=200, null=True)
    email5      = models.CharField(max_length=200, null=True)
    email6      = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nome

class Lista(models.Model):
    id_credor   = models.ForeignKey(Credor, on_delete=models.CASCADE)
    nome        = models.CharField(max_length=128)
    tipoemail   = models.IntegerField()
    diasvenc    = models.IntegerField()
    horadisparo = models.TimeField()
    mensagem    = models.TextField()

    def __str__(self):
        return self.nome

class Operacao(models.Model):
    id_credor   = models.ForeignKey(Credor, on_delete=models.CASCADE)
    id_cliente  = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_op   = models.IntegerField()
    nome_op     = models.CharField(max_length=255, null=True)
    vencimento  = models.DateTimeField(null=True)
    nome_aluno  = models.CharField(max_length=255, null=True)
    descricao   = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.numero_op

class User_Credor(models.Model):
    user_id     = models.ForeignKey(User, on_delete=models.CASCADE)
    credor_id   = models.ForeignKey(Credor, on_delete=models.CASCADE)

    def __str__(self):
        return 'Usuário: ' + str(self.user_id.id) + ' Credor: ' + str(self.credor_id.id)