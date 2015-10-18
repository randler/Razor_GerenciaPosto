from django.db import models
from django.db import models

class novoGasto(models.Model):
    gasto_id = models.AutoField(primary_key = True)
    litros_abastecido = models.DecimalField(max_digits=3, decimal_places= 3)
    tipo_abastecido = models.CharField(max_length=20)
    data_abastecido = models.DateField()
    preco_abastecido = models.DecimalField(max_digits=4, decimal_places=3)
    nome_posto = models.CharField(max_length=20)
    km_atual = models.DecimalField(max_digits=6, decimal_places=6)
    descricao = models.CharField(max_length=60)
