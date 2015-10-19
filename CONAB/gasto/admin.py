from django.contrib import admin
from CONAB.gasto.models import novoGasto

class novoGastoAdmin(admin.ModelAdmin):
    model = novoGasto
    list_display = ['nome_posto','tipo_abastecido','preco_abastecido','litros_abastecido','data_abastecido','descricao','km_atual']
    search_fields = ['nome_posto']
    save_on_top = True
admin.site.register(novoGasto, novoGastoAdmin)