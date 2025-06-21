from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("add_recipe"))
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect(reverse("login_page"))


def register(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        # save data to database
        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        return redirect(reverse("login_page"))
    else:
        return render(request, "register.html")


# Create your views here.
@login_required(login_url="/login/")
def add_recipe(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("recipe_name")
        description = data.get("recipe_description")
        image = request.FILES.get("recipe_image")
        # save data to database
        Recipe.objects.create(
            recipe_name=name, recipe_description=description, recipe_image=image
        )
        return redirect(reverse("add_recipe"))
    else:
        recipes = Recipe.objects.all()
        search_key = request.GET.get("search")
        if search_key:
            recipes = recipes.filter(recipe_name__icontains=search_key)
        return render(request, "recipe_front.html", context={"recipes": recipes})
    

@login_required(login_url="/login/")
def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect(reverse("add_recipe"))

@login_required(login_url="/login/")
def update_recipe(request, id):
    if request.method == "POST":
        data = request.POST
        name = data.get("recipe_name")
        description = data.get("recipe_description")
        recipe = Recipe.objects.get(id=id)

        recipe.recipe_name = name
        recipe.recipe_description = description

        if "recipe_image" in request.FILES:
            recipe.recipe_image = request.FILES.get("recipe_image")

        recipe.save()
        return redirect(reverse("add_recipe"))
    else:
        recipe = Recipe.objects.get(id=id)
        return render(request, "update_recipe.html", context={"recipe": recipe})
