'''This module is for adding models and fields to the form'''

from django import forms
from recipe.models import Recipe

class RecipeForm(forms.ModelForm):# pylint: disable=R0903
    '''This class is to add the model 'Recipe' to the Recipe form'''
    class Meta: # pylint: disable=C1001,R0903,W0232
        '''This class is used to add Recipe model to the Recipe form'''
        model = Recipe
