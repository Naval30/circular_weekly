'''
This Module will have all the unit test for hte user profile
'''

from django.test import TestCase
from django.core.exceptions import ValidationError

from userprofile.models import zip_validate
#from userprofile.models import UserProfile
#from django.contrib.auth.models import User

# Create your tests here.

class UserPrfileTestValidation(TestCase):
    '''
    In this class we are testing the validaiton fucntion for the zip code
    '''
    def test_zip_code_is_5_long(self): # pylint: disable=C0103
        '''
        Testting if the zip code filed is 5 digit long
        '''
        test = u'11385'
        self.assertEqual(zip_validate(test), None)

    def test_zip_code_error_if_not_5_long(self): # pylint: disable=C0103
        '''
        Testting that validataioneroor is raised if zip code filed is less
        them 5 digit long
        '''
        test = u'113'
        self.assertRaises(ValidationError, zip_validate, test)

    def test_zip_code_error_if_has_not_only_digit(self): # pylint: disable=C0103
        '''
        Testting that validataioneroor is raised if zip code filed is has
        any thing eles but unmber in int.
        '''
        test = u'111I1'
        self.assertRaises(ValidationError, zip_validate, test)
