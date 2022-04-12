from django.db import models

# Create your models here.



class Contrato(models.Model):
    entidade = models.CharField(max_length=30)

    def __str__(self):
        return self.entidade