from django.db import models

class Combustivel(models.Model):
    class Meta:
        ordering = ('-data_abastecido',)
        verbose_name_plural = 'Combustivel'

    TIPO_COMBUSTIVEL = (
        (u'gasolina', u'Gasolina'),
        (u'diesel',u'Diesel'),
        (u'alcool',u'Alcool')
        )
    gasto_id = models.AutoField(primary_key = True)
    litros_abastecido = models.FloatField()
    tipo_abastecido = models.CharField(max_length=20,choices=TIPO_COMBUSTIVEL, verbose_name="Tipo de Combustivel")
    data_abastecido = models.DateField()
    preco_abastecido = models.FloatField()
    nome_posto = models.CharField(max_length=20)
    km_atual = models.FloatField()
    descricao = models.TextField(max_length=60)

class Conveniencia(models.Model):
    gasto_conv_id = models.AutoField(primary_key=True)
    nome_conveniencia = models.CharField(max_length=50)
    preco_conveniencia = models.FloatField()
    descricao_conveniencia = models.TextField(max_length=50)
    class Meta:
        verbose_name_plural = 'Coveniencia'