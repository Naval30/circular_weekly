""" Navigates to the register page on Firefox browser and tests the name of the head tag on Register page"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/register/")
        self.assertIn("Sign up", driver.title)
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()