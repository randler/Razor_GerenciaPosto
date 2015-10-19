from django.contrib import admin
from CONAB.gasto.models import Combustivel,Conveniencia

class combustivelAdmin(admin.ModelAdmin):
    model = Combustivel
    list_display = ['nome_posto','tipo_abastecido','preco_abastecido','litros_abastecido','data_abastecido','descricao','km_atual']
    search_fields = ['nome_posto']
    save_on_top = True
admin.site.register(Combustivel, combustivelAdmin)

class convenienciaAdmin(admin.ModelAdmin):
    model = Conveniencia
    list_display = ['descricao_conveniencia','preco_conveniencia']
    search_fields = ['descricao_conveniencia']
    save_on_top = True
admin.site.register(Conveniencia, convenienciaAdmin)
