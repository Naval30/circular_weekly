"""Navigates to every page of the website to check if its up and running"""


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()


    def test_search_in_python1(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com")
        self.assertIn("Weekly Circular - Home page", driver.title)  
        driver.close()


    def test_search_in_python2(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/about/")
        self.assertIn("Weekly Circular - About", driver.title)
        driver.close()    


    def test_search_in_python3(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/contact/")
        self.assertIn("Weekly Circular - Contact", driver.title)  
        driver.close()   


    def test_search_in_python4(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/login/")
        self.assertIn("Log in", driver.title) 
        driver.close()    


    def test_search_in_python5(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/register/")
        self.assertIn("Sign up", driver.title) 
        driver.close()
        

    def test_search_in_python6(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/deals/")
        self.assertIn("Deals", driver.title) 
        driver.close()    
    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()    