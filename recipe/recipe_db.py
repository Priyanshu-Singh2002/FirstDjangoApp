# In this i write all the functions that interact with the database for recipe app.
from .models import Recipe
from django.contrib.auth.models import User

def get_recipes(user_id):
    query = Recipe.objects.filter(user_id=user_id)
    return query