'''
def get_profile_model():
    if (not hasattr(settings, 'AUTH_USER_MODULE')) or
    (not settings.AUTH_USER_MODULE):
        raise SiteProfileNotAvailable
    profile_mod = get_model(*settings.AUTH_USER_MODULE.split('.'))
    if profile_mod is None:
        raise SiteProfileNotAvailable

    return profile_mod

def get_profile_form():
    profile_mod = get_profile_model()

    class _ProfileForm(forms.ModelForm):
        class Meta:
            model = profile_mod
            exclude = ('user',)
    return _ProfileForm
'''

#from django import forms
#from django.conf import settings
#from django.contrib.auth.models import SiteProfileNotAvailable
#from django.db.models import get_model
#from django.contrib.auth.models import User
#from django.core.exceptions import ValidationError

from userprofile.models import UserProfile

def create_profile(user):
    '''
    Fucntio to crate a user profile in the database.
    '''
    profile_obj = UserProfile
    # pylint: disable=E1101
    profile_obj.objects.create(user=user)
    # pylint enable=E1101
    return profile_obj
