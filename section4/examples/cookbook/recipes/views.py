from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Recipe, Ingredient

from django.forms import ModelForm

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'price']  # For listing no User please


# Create your views here.
def index(request):
    context = {
        "recipes": Recipe.objects.all()
    }
    return render(request, "recipes/index.html", context)


def recipe(request, recipe_id):
    i = 0

    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    context = {
        "recipe": recipe,
        "ingredients": recipe.ingredients.all(),
        "non_ingredients": Ingredient.objects.exclude(recipe=recipe).all()
    }
    return render(request, "recipes/recipe.html", context)


def add(request, recipe_id):
    try:
        ingredient_id = int(request.POST["ingredient"])
        recipe = Recipe.objects.get(pk=recipe_id)
        ingredient = Ingredient.objects.get(pk=ingredient_id)
    except KeyError:
        return render(request, "recipes/error.html", {"message": "No selection."})
    except Recipe.DoesNotExist:
        return render(request, "recipes/error.html", {"message": "No recipe."})
    except Ingredient.DoesNotExist:
        return render(request, "recipes/error.html", {"message": "No ingredient."})

    # associate with recipe
    ingredient.recipe.add(recipe)

    # recipe.ingredients.add(recipe)

    return HttpResponseRedirect(reverse("recipe", args=(recipe_id,)))



@csrf_exempt
def ingredient(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IngredientForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            ingredient = form.save(commit=False)  # Pre-save

            ingredient.chef_name = 'Some chef'  # Plug in fields not supplied by form
            ingredient.save()  # Save to DB

            return HttpResponseRedirect(reverse("index"))




    return render(request, "recipes/ingredient.html", {'form': IngredientForm()})
