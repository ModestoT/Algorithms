#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Get how many batches can be made with the available ingredients compared to the recipes needed ingredients
  # Compare the dictonaries of the recipe to the ingredients 
  # if the ingredients dic does not have one of the keys or not enough of one ingredient from the recipe return 0
  # else get the number of times the recipe can be made
  current_difference = None

  for i, k in recipe.items():
    if i in ingredients:
      if k <= ingredients[i]:
        difference = ingredients[i] // k
  
        if current_difference:
          if current_difference > difference:
            current_difference = difference

        else:
          current_difference = difference

      else:
        return 0

    else:
      return 0

  return current_difference
   


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 2 }
  ingredients = { 'milk': 200}
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))