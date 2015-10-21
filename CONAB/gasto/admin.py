from django.contrib import admin
from CONAB.gasto.models import Combustivel,Servico

class combustivelAdmin(admin.ModelAdmin):
    model = Combustivel
    list_display = ['nome_posto','tipo_abastecido','preco_abastecido','litros_abastecido','data_abastecido','descricao','km_atual']
    list_filter = ['nome_posto','tipo_abastecido']
    search_fields = ['nome_posto']
    save_on_top = True
admin.site.register(Combustivel, combustivelAdmin)

class servicoAdmin(admin.ModelAdmin):
    model = Servico
    list_display = ['nome_servico','preco_servico']
    search_fields = ['descricao_servico']
    save_on_top = True
admin.site.register(Servico, servicoAdmin)
