from django.db import models

# Create your models here.
CONTRATO_CHOICES = (
        ('A', 'ATIVO'),
        ('F', 'FINALIZADO')
)


class Contrato(models.Model):
    entidade = models.CharField(max_length=30)
    contrato = models.CharField(max_length=100)
    estado = models.CharField(max_length=1,choices=CONTRATO_CHOICES)
    numero = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    data_inicio = models.DateField(blank=True, null=True)
    contato = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    email = models.EmailField(blank = True, null = True)
    endereço = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    prazo = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    detalhes = models.TextField(blank = True)
    digitalizado = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    def __str__(self):
        return self.entidade