from django.shortcuts import render,redirect, reverse

from .models import *

# Create your views here.
def add_recipe(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('recipe_name')
        description = data.get('recipe_description')
        image = request.FILES.get('recipe_image')
        # save data to database 
        Recipe.objects.create(
            recipe_name=name,
            recipe_description=description,
            recipe_image=image
        )
        return redirect(reverse('add_recipe'))
    else:
        recipes = Recipe.objects.all() 
        return render(request, 'recipe_front.html', context={'recipes': recipes})

def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect(reverse('add_recipe'))

def update_recipe(request, id):
    if request.method == 'POST':
        data = request.POST
        name = data.get('recipe_name')
        description = data.get('recipe_description')
        recipe = Recipe.objects.get(id=id)
        
        recipe.recipe_name=name
        recipe.recipe_description=description

        if 'recipe_image' in request.FILES:
           recipe.recipe_image = request.FILES.get('recipe_image')

        recipe.save()
        return redirect(reverse('add_recipe'))
    else:
        recipe = Recipe.objects.get(id=id)
        return render(request, 'update_recipe.html', context={'recipe': recipe})