from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'George Silva'
    })
# esta pasta recipes dentro de templates e usada para dar um nome especifico ao arquivo home para o django não confundir com outro.


def contato(request):
    return render(request, 'apagar/temp.html')


def sobre(request):
    return HttpResponse('sobre')
