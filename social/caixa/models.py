from django.conf import settings
from django.db import models
from django.utils import timezone


class Comida(models.Model):

    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits= 3, decimal_places= 2)

    def __str__(self):
        return self.descricao


class Pedidos(models.Model):

    OPCOES = (
        ("arroz", "arroz" ),
        ("feijão", "feijão"),
        ("macarrão", "macarrão")
    );

    QUANTIDADE = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
        (11, "11"),
        (12, "12"),
        (13, "13"),
        (14, "14"),
        (15, "15"),
        (16, "16"),
        (17, "17"),
        (18, "18"),
        (19, "19"),
        (20, "20"),
    );

    item1 = models.CharField(null=False, choices=OPCOES, max_length=30, default=OPCOES[0])
    qtd_item1 = models.IntegerField(default=1, choices=QUANTIDADE)

    item2 = models.CharField(null=True, choices=OPCOES, max_length=30, blank=True)
    qtd_item2 = models.IntegerField(null=True, choices=QUANTIDADE, blank=True)

    item3 = models.CharField(null=True, choices=OPCOES, max_length=30)
    qtd_item3 = models.IntegerField(null=True, choices=QUANTIDADE)

    item4 = models.CharField(null=True, choices=OPCOES, max_length=30)
    qtd_item4 = models.IntegerField(null=True, choices=QUANTIDADE)

    item5 = models.CharField(null=True, choices=OPCOES, max_length=30)
    qtd_item5 = models.IntegerField(null=True, choices=QUANTIDADE)

    item6 = models.CharField(null=True, choices=OPCOES, max_length=30)
    qtd_item6 = models.IntegerField(null=True, choices=QUANTIDADE)

    item7 = models.CharField(null=True, choices=OPCOES, max_length=30)
    qtd_item7 = models.IntegerField(null=True, choices=QUANTIDADE)

    item8 = models.CharField(null=True, choices=OPCOES, max_length=30)
    qtd_item8 = models.IntegerField(null=True, choices=QUANTIDADE)

    item9 = models.CharField(null=True, choices=OPCOES, max_length=30)
    qtd_item9 = models.IntegerField(null=True, choices=QUANTIDADE)
