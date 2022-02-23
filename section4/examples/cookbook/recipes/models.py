from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

class Recipe(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recepies")
    prep_time = models.IntegerField() # in minutes

    def __str__(self):
       return f"{self.name} type of {self.category} takes {self.prep_time} min"
        # return f"{self.category}:{self.name}:{self.prep_time} min"


class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    recipe = models.ManyToManyField(Recipe, blank=True, related_name="ingredients")

    chef_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"


    def triple_price(self):
        return self.price * 3






# # Obj of Cake
# category = Category.objects.get(name='Cake')

# # Option 1 - BAD 
# recepies = Recipe.objects.filter(category__name  = 'Cake')  # Not good

# # Option 2 - GOOD
# recepies = category.recipes.all()