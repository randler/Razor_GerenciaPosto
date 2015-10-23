# Create your views here.
# coding: utf-8
from django.shortcuts import render_to_response
from django.views.generic import ListView
from CONAB.gasto.models import Combustivel, Servico
from django.db.models import Avg, Max, Min, Sum

#def home(request):
 #   return render(request, 'inicio/index.html',{})

def abastecimentos(request):
	abastecimentos = Combustivel.objects.all().count()
	soma = Combustivel.objects.aggregate(Sum('preco_abastecido'))
 	somaConv = Combustivel.objects.aggregate(Sum('preco_conveniencia'))
	somaServ = Servico.objects.aggregate(Sum('preco_servico'))
 	return render_to_response('gasto/abastecimentos.html',{'abast':abastecimentos,'s':soma, 'somaConv': somaConv, 'somaServ':somaServ})