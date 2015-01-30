'''This module calls the yummly API, retrieves the recipe
   and displays it to the user.'''
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.http import HttpResponse
import json
from yummly import Client
from recipe.forms import RecipeForm


def get_recipe(request):
    '''This function calls the yummly API and retrieves recipe data'''
    client = Client(api_id='3d16b896',
                    api_key='ad2bc866586798e1e659e988442cafb3')
    if request.method == 'POST':
        form = RecipeForm(request.POST) # pylint: disable=E1120
        #print form.errors
        if form.is_valid(): # pylint: disable=E1101
            recipe_name = request.POST.get('q', "")
            allowed_ingredients = request.POST.get('AllowedIngredients', "")
            excluded_ingredients = request.POST.get('ExcludedIngredients', "")
            allowed_cuisine = request.POST.get('allowedCuisine', "")
            allowed_course = request.POST.get('allowedCourse', "")
            options = {
                'q': recipe_name,
                'start': 0,
                'maxResult': 5,
                'requirePicutres': True,
                'allowedIngredient[]': [allowed_ingredients],
                'excludedIngredient[]': [excluded_ingredients],
                'allowedCuisine[]': [allowed_cuisine],
                'allowedCourse[]' : [allowed_course],
                'maxTotalTimeInSeconds': 3600,
                'facetField[]': ['ingredient', 'diet'],
                'flavor.sweet.min': 0,
                'flavor.sweet.max': 0.5,
                'nutrition.FAT.min': 0,
                'nutrition.FAT.max': 15
                }
            results2 = client.search(**options) # pylint: disable=W0142
            for match in results2.matches: #displaying 5 options in the terminal
                print 'Recipe ID:', match.id
                print 'Recipe:', match.recipeName
                print 'Rating:', match.rating
                for i in match.ingredients:
                    print 'Ingredients:', i
            match = results2.matches[0]
            match1 = results2.matches[1]
            recipe = client.recipe(match.id) #1st recipe
            recipe1 = client.recipe(match1.id) #2nd recipe
            print recipe
            response_dict = {}
            response_dict.update({'id': recipe.id})
            response_dict.update({'name': recipe.name})
            response_dict.update({'totalTime': recipe.totalTime})
            response_dict.update({'Ingredients': recipe.ingredientLines})
            response_dict.update({'url':  recipe.attribution.url})
            response_dict.update({'Rating': recipe.rating})
            response_dict.update({'id1': recipe1.id})
            response_dict.update({'name1': recipe1.name})
            response_dict.update({'totalTime1': recipe1.totalTime})
            response_dict.update({'Ingredients1': recipe1.ingredientLines})
            response_dict.update({'url1':  recipe1.attribution.url})
            response_dict.update({'Rating1': recipe1.rating})
            return HttpResponse(json.dumps(response_dict),
                                content_type='application/javascript')
        else:
            return HttpResponse("not valid form")
    else:
        form_recipe = RecipeForm() # pylint: disable=E1120
    ctx = {'form': form_recipe}
    return render_to_response('recipe_form.html',
                              ctx,
                              context_instance=RequestContext(request),
                             )
