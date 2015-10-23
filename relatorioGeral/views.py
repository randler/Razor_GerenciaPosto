# Create your views here.
from django.db.models.sql.aggregates import Sum
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from CONAB.gasto.models import Combustivel


class relatorioGeral(ListView):
    template_name = 'relatorio/relatorio.html'

    model = Combustivel

    context_object_name = 'combustivel'
