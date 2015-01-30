""" Take screenshot of website whenever required for further evaluation"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()


    def test_search_in_python1(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com")
        driver.save_screenshot('screenshotHome.png')   
        driver.close()    


    def test_search_in_python2(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/about/")
        driver.save_screenshot('screenshotAbout.png')   
        driver.close()


    def test_search_in_python3(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/contact/")
        driver.save_screenshot('screenshotContact.png')   
        driver.close() 


    def test_search_in_python4(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/login/")
        driver.save_screenshot('screenshotLogin.png')   
        driver.close()


    def test_search_in_python5(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/register/")
        driver.save_screenshot('screenshotRegister.png')   
        driver.close()    


    def test_search_in_python6(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/deals/") 
        driver.save_screenshot('screenshotDeals.png')   
        driver.close()    


    def test_search_in_python7(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/recipe/") 
        driver.save_screenshot('screenshotRecipe.png')   
        driver.close()      

        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()    