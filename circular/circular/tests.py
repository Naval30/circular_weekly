'''This module is to write testcases'''
from django.contrib.auth.models import User
from django.test import TestCase
import unittest # pylint: disable=W0611
from registration import forms
from registration.models import RegistrationProfile # pylint: disable=W0611
from circular.models import Product, Store, StoreLocation # pylint: disable=W0611


class RegistrationFormTests(TestCase): # pylint: disable=R0904
    '''Test the default registration forms.'''
    def test_registration_form(self):
        '''Test that ``RegistrationForm`` enforces username constraints
        and matching passwords.'''
        # Create a user so we can verify that duplicate usernames aren't
        # permitted.
        User.objects.create_user('alice', 'alice@example.com', 'secret')

        invalid_data_dicts = [
            # Non-alphanumeric username.
            {'data': {'username': 'weekly/circular',
                      'email': 'circular@example.com',
                      'password1': 'mashup',
                      'password2': 'mashup'},
             'error': ('username', [u"May contain only letters, "\
                                     "numbers and @/./+/-/_."])},
            # Already-existing username.
            {'data': {'username': 'weekly',
                      'email': 'weekly@example.com',
                      'password1': '12345',
                      'password2': '12345'},
             'error': ('username', [u"A user with that username "\
                                     "already exists."])},
            # Mismatched passwords.
            {'data': {'username': 'ana',
                      'email': 'ana@example.com',
                      'password1': 'ana',
                      'password2': '12345'},
             'error': ('__all__', [u"The two password "\
                                    "fields didn't match."])},
            ]

        for invalid_dict in invalid_data_dicts:
            form = forms.RegistrationForm(data=invalid_dict['data']) # pylint: disable=E1120,E1123
            self.failIf(False == form.is_valid()) # pylint: disable=E1101
            self.assertEqual(form.errors[invalid_dict['error'][0]], # pylint: disable=E1101
                             invalid_dict['error'][1])

        form = forms.RegistrationForm(data={'username': 'ana', # pylint: disable=E1120,E1123
                                            'email': 'ana@example.com',
                                            'password1': '1234',
                                            'password2': '1234'})
        self.failUnless(form.is_valid()) # pylint: disable=E1101

    def test_reg_form_unique_email(self):
        """
        Test that ``RegistrationFormUniqueEmail`` validates uniqueness
        of email addresses.

        """
        # Create a user so we can verify that duplicate addresses
        # aren't permitted.
        error_msg = {"This email address is already in use."\
                     "Please supply a different email address."}
        User.objects.create_user('alice', 'alice@example.com', 'secret')
        form = forms.RegistrationFormUniqueEmail(data={'username': 'foo', # pylint: disable=E1120,E1123
                                                       'email':\
                                                         'alice@example.com',
                                                       'password1': 'foo',
                                                       'password2': 'foo'})
        self.failIf(form.is_valid()) # pylint: disable=E1101
        self.assertEqual(form.errors['email'], [error_msg]) # pylint: disable=E1101
        form = forms.RegistrationFormUniqueEmail(data={'username': 'foo', # pylint: disable=E1120,E1123
                                                       'email'\
                                                        : 'foo@example.com',
                                                       'password1': 'foo',
                                                       'password2': 'foo'})
        self.failUnless(form.is_valid()) # pylint: disable=E1101

    def test_reg_form_no_free_email(self):
        '''Test that ``RegistrationFormNoFreeEmail`` disallows
        registration with free email addresses.'''
        base_data = {'username': 'ana',
                     'password1': '12345',
                     'password2': '12345'}
        msg = {'Registration using free email addresses is prohibited. '\
                'Please supply a different email address.'}
        for domain in forms.RegistrationFormNoFreeEmail.bad_domains:
            invalid_data = base_data.copy()
            invalid_data['email'] = u"ana@%s" % domain
            form = forms.RegistrationFormNoFreeEmail(data=invalid_data) # pylint: disable=E1120,E1123
            self.failIf(form.is_valid()) # pylint: disable=E1101
            self.assertEqual(form.errors['email'], [msg]) # pylint: disable=E1101,E1123
        base_data['email'] = 'ana@example.com'
        form = forms.RegistrationFormNoFreeEmail(data=base_data) # pylint: disable=E1120,E1123
        self.failUnless(form.is_valid()) # pylint: disable=E1101

class ProductTestCase(TestCase): # pylint: disable=R0904
    '''Testing Product Model'''
    def setup(self): # pylint: disable=R0201
        ''' Creating product object'''
        Product.objects.create(product_name='xyz', # pylint: disable=E1101
                               discount_price='12', regolar_price='15',
                               valid_trough='04-02-2014',
                               notes='this is a good deal')
        Product.objects.create(product_name='abc', # pylint: disable=E1101
                               discount_price='35', regolar_price='45',
                               valid_trough='04-12-2014',
                               notes='this is the best deal')
    def product_price_test(self):
        '''Testing prduct price'''
        xyz = Product.object.get(product_name="xyz") # pylint: disable=E1101
        abc = Product.object.get(product_name="abc") # pylint: disable=E1101
        self.assertEqual(xyz.discount_price, '12')
        self.assertEqual(abc.discount_price, '35')
'''
class RegistrationTestCase(TestCase):
    """
    Base class for the test cases; this sets up two users -- one
    expired, one not -- which are used to exercise various parts of
    the application.
    
    """
    def setUp(self):
        self.sample_user = RegistrationProfile.objects.create_inactive_user(username='alice',
                                                                            password='secret',
                                                                            email='alice@example.com')
        self.expired_user = RegistrationProfile.objects.create_inactive_user(username='bob',
                                                                             password='swordfish',
                                                                             email='bob@example.com')
        self.expired_user.date_joined -= datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS + 1)
        self.expired_user.save()
        
        
class RegistrationModelTests(RegistrationTestCase):
    """
    Tests for the model-oriented functionality of django-registration,
    including ``RegistrationProfile`` and its custom manager.
    
    """
    def test_new_user_is_inactive(self):
        """
        Test that a newly-created user is inactive.
        
        """
        self.failIf(self.sample_user.is_active)

    def test_registration_profile_created(self):
        """
        Test that a ``RegistrationProfile`` is created for a new user.
        
        """
        self.assertEqual(RegistrationProfile.objects.count(), 2)

    def test_activation_email(self):
        """
        Test that user signup sends an activation email.
        
        """
        self.assertEqual(len(mail.outbox), 2)

    def test_activation(self):
        """
        Test that user activation actually activates the user and
        properly resets the activation key, and fails for an
        already-active or expired user, or an invalid key.
        
        """
        # Activating a valid user returns the user.
        self.failUnlessEqual(RegistrationProfile.objects.activate_user(RegistrationProfile.objects.get(user=self.sample_user).activation_key).pk,
                             self.sample_user.pk)
        
        # The activated user must now be active.
        self.failUnless(User.objects.get(pk=self.sample_user.pk).is_active)
        
        # The activation key must now be reset to the "already activated" constant.
        self.failUnlessEqual(RegistrationProfile.objects.get(user=self.sample_user).activation_key,
                             RegistrationProfile.ACTIVATED)
        
        # Activating an expired user returns False.
        self.failIf(RegistrationProfile.objects.activate_user(RegistrationProfile.objects.get(user=self.expired_user).activation_key))
        
        # Activating from a key that isn't a SHA1 hash returns False.
        self.failIf(RegistrationProfile.objects.activate_user('foo'))
        
        # Activating from a key that doesn't exist returns False.
        self.failIf(RegistrationProfile.objects.activate_user(sha.new('foo').hexdigest()))

    def test_account_expiration_condition(self):
        """
        Test that ``RegistrationProfile.activation_key_expired()``
        returns ``True`` for expired users and for active users, and
        ``False`` otherwise.
        
        """
        # Unexpired user returns False.
        self.failIf(RegistrationProfile.objects.get(user=self.sample_user).activation_key_expired())

        # Expired user returns True.
        self.failUnless(RegistrationProfile.objects.get(user=self.expired_user).activation_key_expired())

        # Activated user returns True.
        RegistrationProfile.objects.activate_user(RegistrationProfile.objects.get(user=self.sample_user).activation_key)
        self.failUnless(RegistrationProfile.objects.get(user=self.sample_user).activation_key_expired())

    def test_expired_user_deletion(self):
        """
        Test that
        ``RegistrationProfile.objects.delete_expired_users()`` deletes
        only inactive users whose activation window has expired.
        
        """
        RegistrationProfile.objects.delete_expired_users()
        self.assertEqual(RegistrationProfile.objects.count(), 1)

    def test_management_command(self):
        """
        Test that ``manage.py cleanupregistration`` functions
        correctly.
        
        """
        management.call_command('cleanupregistration')
        self.assertEqual(RegistrationProfile.objects.count(), 1)
''' # pylint: disable=W0105
