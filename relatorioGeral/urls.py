
from django.conf.urls import patterns, include, url
from relatorioGeral.views import relatorioGeral

urlpatterns = patterns('',

    url(r'^relatorio_geral/$' , relatorioGeral.as_view(), name='relatorio_geral'),
)

