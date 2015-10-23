# Create your views here.
# coding: utf-8
from django.shortcuts import render_to_response
from CONAB.gasto.models import Combustivel
from django.db.models import Avg, Max, Min, Sum

#def home(request):
 #   return render(request, 'inicio/index.html',{})

def abastecimentos(request):
	abastecimentos = Combustivel.objects.all().count()
	soma = Combustivel.objects.aggregate(Sum('preco_abastecido'))
 	return render_to_response('abastecimentos.html',{'abast':abastecimentos,'s':soma})

