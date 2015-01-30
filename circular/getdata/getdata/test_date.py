'''
Here we will have all unit test for our code
'''
from datetime import date
from datetime import timedelta

from django.test import TestCase
from getdata.utils import deal_valid

class ScarpyValidDateTestCase(TestCase):
    '''
    Here we are testing the deal_valid function.
    '''
    def test_valid_from(self):
        '''
        Testing the case of Valid from "month day - month day"
        '''
        valid_from = "Valid from May 09 - May 15"
        self.assertEqual(
            [date(2014, 05, 9), date(2014, 05, 15)],
            deal_valid(valid_from))

    def test_deal_expires(self):
        '''
        Testing the case of Valid from "Deal expires today"
        '''
        valid_from = "Deal expires today."
        self.assertEqual(
            [None, date.today()],
            deal_valid(valid_from))

    def test_deal_expires_in(self):
        '''
        Testing the case of Valid from "Deal expires in 5 days"
        '''
        my_date = date.today() + timedelta(5)
        valid_from = "Deal expires in 5 days."
        self.assertEqual([None, my_date], deal_valid(valid_from))

    def test_no_date_deal_expiration(self):
        '''
        Testeing if non o the option is there.
        '''
        valid_from = "Some day"
        self.assertRaises(TypeError, lambda: deal_valid(valid_from))

    def test_month_full_name(self):
        '''
        This test that we gat the correct month for long month name
        '''
        valid_from="Valid From May 09 - August 25"
        self.assertEqual([date(2014, 05, 9), date(2014, 8, 25)],
                deal_valid(valid_from))
