from django.contrib import admin
from CONAB.relatorio.models import Relatorio


class relatorioAdmin(admin.ModelAdmin):
    model = Relatorio
    list_display = ['nome_posto','tipo_abastecido','preco_abastecido','litros_abastecido','data_abastecido','descricao','km_atual']
    list_filter = ['nome_posto','tipo_abastecido']
    search_fields = ['nome_posto']
    save_on_top = True
admin.site.register(Relatorio, relatorioAdmin)

