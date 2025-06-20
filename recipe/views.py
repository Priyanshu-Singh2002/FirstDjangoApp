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