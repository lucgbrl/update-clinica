from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class pai(models.Model):
    class Meta:
         verbose_name="Prontuario de atendimento integral"
         verbose_name_plural="Prontuarios de atendimento integral"
    # Dados básicos
    #info basica
    nome = models.CharField("Nome", max_length=255)
    sobrenome = models.CharField("Sobrenome", max_length=255)
    data_de_Nascimento = models.DateField(default = timezone.now, blank = True, null=True)
    nome_pai = models.CharField("Pai", max_length=255, blank = True, null = True)
    nome_mae = models.CharField("Mãe", max_length=255, blank = True, null = True)
    data_de_registro = models.DateField(verbose_name="Data de cadastro", default = timezone.now, null = True)
    #Dados sociais
    
    cpf = models.CharField("CPF", max_length=255, blank = True, null = True)
    rg = models.CharField("RG", max_length=255, blank = True, null = True)
    profissao = models.CharField("Profissao", max_length=255, blank = True, null = True)
    etnia = models.CharField("Etnia", max_length=32)
    sexo = models.CharField(max_length=24)
    naturalidade = models.CharField("Naturalidade", max_length=255, blank = True, null = True)

    #endereco
    uf = models.CharField("UF", max_length=32)
    cidade = models.CharField("Cidade", max_length=32)
    bairro = models.CharField("Bairro", max_length=32)
    rua = models.CharField("Rua",  max_length= 32)
    numro = models.IntegerField("Nº")
    cep = models.CharField("CEP", max_length=8)

    #contato
    cel = models.CharField("Celular", max_length=11)
    Fixo = models.CharField("Fixo", max_length=11)
    email = models.CharField("E-mail", max_length=255)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Profissional responsável", null = True)

    def publish(self):
            self.data_de_Nascimento = timezone.now()
            self.save()

    #retorna info para a tabela
    def __str__(self):
            #return self.nome
            return self.nome
            return self.id 
            return self.cpf 
            return self.telefone
