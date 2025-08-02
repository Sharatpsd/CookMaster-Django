from django.shortcuts import render

# Create your views here.
from .models import Recipe

def recipe_list(request):
    recipes=Recipe.objects.all()
    return render(request,'recipes/recipe_list.html',{'recipes':recipes})
