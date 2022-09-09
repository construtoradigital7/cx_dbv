from django.db import models

class Lanche(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return self.descricao



class Bebida(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return self.descricao
