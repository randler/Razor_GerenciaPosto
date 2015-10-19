from django.db import models

class Combustivel(models.Model):
    gasto_id = models.AutoField(primary_key = True)
    litros_abastecido = models.FloatField()
    tipo_abastecido = models.CharField(max_length=20)
    data_abastecido = models.DateField()
    preco_abastecido = models.FloatField()
    nome_posto = models.CharField(max_length=20)
    km_atual = models.FloatField()
    descricao = models.CharField(max_length=60)

class Conveniencia(models.Model):
    gasto_conv_id = models.AutoField(primary_key=True)
    descricao_conveniencia = models.CharField(max_length=50)
    preco_conveniencia = models.FloatField()

