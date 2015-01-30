'''This module is for creating models'''
from django.db import models
#from django.utils.encoding import smart_unicode

class Recipe(models.Model):
    '''This class creates the model Recipe'''
    Cuisine_choices = (
        ("American", "American"),
        ("Italian", "Italian"),
        ("Asian", "Asian"),
        ("Mexican", "Mexican"),
        ("Southern & Soul Food", "Southern & Soul Food"),
        ("French", "French"),
        ("Indian", "Indian"),
        ("Barbecue", "Barbecue"),
        ("Cajun & Creole", "Cajun & Creole"),
        ("Chinese", "Chinese"),
        ("Mediterranean", "Mediterranean"),
        ("Greek", "Greek"),
        ("Spanish", "Spanish"),
        ("Southwestern", "Southwestern"),
        ("Japanese", "Japanese"),
        ("Irish", "Irish"),
        ("Moroccan", "Moroccan"),
        ("Hawaiin", "Hawaiin"),
        ("Swedish", "Swedish"),
        ("Hungarian", "Hungarian"),
        ("German", "German"),
        ("Portugese", "Portugese"),
        ("Thai", "Thai"),
    )
    Course_choices = (
        ("Main Dishes", "Main Dishes"),
        ("Desserts", "Desserts"),
        ("Soups", "Soups"),
        ("Breakfast and Brunch", "Breakfast and Brunch"),
        ("Breads", "Breads"),
        ("Salads", "Salads"),
        ("Appetizers", "Appetizers"),
        ("Lunch and Snacks", "Lunch and Snacks"),
        ("Side Dishes", "Side Dishes"),
        ("Cocktails", "Cocktails"),
        ("Condiments and Sauces", "Condiments and Sauces"),
        ("Beverages", "Beverages"),
    )
    Allergy_choices = (
        ("Dairy", "Dairy"),
        ("Egg", "Egg"),
        ("Gluten", "Gluten"),
        ("Peanut", "Peanut"),
        ("Seafood", "Seafood"),
        ("Sesame", "Sesame"),
        ("Soy", "Soy"),
        ("Sulfite", "Sulfite"),
        ("Tree Nut", "Tree Nut"),
    )
    Holiday_choices = (
        ("Christmas", "Christmas"),
        ("Thanksgiving", "Thanksgiving"),
        ("NewYear", "NewYear"),
        ("Super Bowl/Game Day", "Super Bowl/Game Day"),
        ("Halloween", "Halloween"),
        ("Hanukkah", "Hanukkah"),
        ("4th of July", "4th of July"),
    )
    Diet_choices = (
        ("Lacto vegetarian", "Lacto vegetarian"),
        ("Ovo vegetarian", "Ovo vegetarian"),
        ("Pescetarian", "Pescetarian"),
        ("Vegan", "Vegan"),
        ("Vegetarian", "Vegetarian"),
    )
    Flavor_choices = (
        ("meaty", "meaty"),
        ("sour", "sour"),
        ("sweet", "sweet"),
        ("salty", "salty"),
        ("piquant", "piquant"),
    )
    q = models.CharField(max_length=50,
                         blank=True, null=True)
    AllowedIngredients = models.CharField(max_length=100,
                                          blank=True, null=True)
    ExcludedIngredients = models.CharField(max_length=100,
                                           blank=True, null=True)
    cuisine = models.CharField(max_length=50, choices=Cuisine_choices,
                               blank=True, null=True)
    course = models.CharField(max_length=50, choices=Course_choices,
                              blank=True, null=True)
    Allergy = models.CharField(max_length=20, choices=Allergy_choices,
                               blank=True, null=True)
    Holiday = models.CharField(max_length=20, choices=Holiday_choices,
                               blank=True, null=True)
    Diet = models.CharField(max_length=20, choices=Diet_choices,
                            blank=True, null=True)
    flavors = models.CharField(max_length=10, choices=Flavor_choices,
                               blank=True, null=True)
