# Create your views here.
from django.shortcuts import render

def home(request):
        context = {'texto': 'Hello World!'}
        return render(request, 'index.html', context)