'''
This module is for adding models and fields
to the User Profile Page.
'''
from django import forms
from django.contrib.auth.models import User

from userprofile.models import UserProfile

class FormUserUpdate(forms.ModelForm): # pylint: disable=R0903
    '''
    This class is to add the model 'User'
    to the User Profile page.
    '''
    class Meta: # pylint: disable=R0903,C1001,W0232
        '''
           This class is to add the model 'User'
           and the fields to User Profile page.
        '''
        model = User
        fields = ('first_name', 'last_name', 'email')

class FormUserProfileUpadte(forms.ModelForm): # pylint: disable=R0903
    '''
    This class is to add the model 'UserProfile'
    to the User Profile page.
    '''
    class Meta: # pylint: disable=R0903,W0232,C1001
        '''
        This class is to add the model 'UserProfile'
        and the fields to User Profile page.
        '''
        model = UserProfile
        fields = ('zip_code', 'allergy', 'diet')
