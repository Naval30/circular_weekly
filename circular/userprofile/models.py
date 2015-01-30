'''
   This module has models and other helper function
               for the user profile.
'''
from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import BaseUserManager
#from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError

def zip_validate(zip_code):
    '''
       Function to validate the zip code which should be
                   numberic and 5 digit long.
    '''
    if len(zip_code) == 5:
        try:
            int(zip_code)
        except:
            raise ValidationError("You can input only numbers in this field")
    else:
        raise ValidationError("The value in this field has to be 5 digit long")

class UserProfile(models.Model):
    '''
       Model for user profile preferances.
    '''
    Allergy_choices = (
        ("N/A", "N/A"),
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
    Diet_choices = (
        ("N/A", "N/A"),
        ("Lacto vegetarian", "Lacto vegetarian"),
        ("Ovo vegetarian", "Ovo vegetarian"),
        ("Pescetarian", "Pescetarian"),
        ("Vegan", "Vegan"),
        ("Vegetarian", "Vegetarian"),
    )
    user = models.OneToOneField(User)
    zip_code = models.CharField(max_length=5,
                                blank=True,
                                null=True,
                                validators=[zip_validate])
    allergy = models.CharField(max_length=20,
                               default='N/A',
                               choices=Allergy_choices)
    diet = models.CharField(max_length=20,
                            default='N/A',
                            choices=Diet_choices)

    def __unicode__(self):
        return u"Profile for %s" % self.user

#User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
