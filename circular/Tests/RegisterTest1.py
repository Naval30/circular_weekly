"""Test to register with a valid username, email id and password"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/register/")
        self.assertIn("Sign up", driver.title)
        element = driver.find_element_by_id("id_username")
        element.send_keys("naval12")
        element = driver.find_element_by_id("id_email")
        element.send_keys("navalnain@yahoo.co.in")
        element = driver.find_element_by_id("id_password1")
        element.send_keys("naval1234")
        element = driver.find_element_by_id("id_password2")
        element.send_keys("naval1234")
        element.send_keys(Keys.RETURN)
        driver.close()
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()