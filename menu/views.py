from django.shortcuts import render
from .models import Recipe
import random

# Create your views here.
def show_menu(request):
    menu = Recipe.objects.all()
    return render(request, "menu/menu.html", {
        "menu" : menu
    })

def show_recipe(request, slug):
    foods = Recipe.objects.all()            
    next_up = foods[:4]
    recipe = Recipe.objects.get(slug = slug)
    return render(request, "menu/recipe.html", {
        "recipe" : recipe,
        "selected_foods" : next_up
    })
        