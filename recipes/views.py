# from django.http import HttpResponse
from django.shortcuts import render

from util.recipes.factory import make_recipe

# importando arquivo fake de teste

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


""" esta pasta recipes dentro de templates e usada para dar um nome especifico ao arquivo home para o django não confundir com outro. """


def recipe(request, id):
    return render(request, 'recipes/partials/recipe_view.html', context={
        recipe: make_recipe()
    })
