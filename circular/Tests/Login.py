"""Attempts to login in with the following details"""



import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()


    """" Valid entries """

    def test_search_in_python1(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/login/")
        self.assertIn("Log in", driver.title)
        element = driver.find_element_by_id("id_username")
        element.send_keys("naval12")
        element = driver.find_element_by_id("id_password")
        element.send_keys("naval12")
        element.send_keys(Keys.RETURN)
        driver.implicitly_wait(20)
        driver.save_screenshot('screenshot01.png')
        self.assertEqual("Weekly Circular - Home page", self.driver.title)
        driver.close()


    """" Invalid entries(incorrect password) """

    def test_search_in_python2(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/login/")
        self.assertIn("Log in", driver.title)
        element = driver.find_element_by_id("id_username")
        element.send_keys("naval12")
        element = driver.find_element_by_id("id_password")
        element.send_keys("naval1234")
        element.send_keys(Keys.RETURN)
        driver.implicitly_wait(20)
        driver.save_screenshot('screenshot02.png')
        self.assertEqual("Registration complete", self.driver.title)
        driver.close


    """" Invalid entries(No password) """

    def test_search_in_python3(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/login/")
        self.assertIn("Log in", driver.title)
        element = driver.find_element_by_id("id_username")
        element.send_keys("naval12")
        element = driver.find_element_by_id("id_password")
        element.send_keys("")
        element.send_keys(Keys.RETURN)
        driver.implicitly_wait(20)
        driver.save_screenshot('screenshot03.png')
        self.assertEqual("Registration complete", self.driver.title)
        driver.close()


    """" Invalid entries(No username) """

    def test_search_in_python4(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/login/")
        self.assertIn("Log in", driver.title)
        element = driver.find_element_by_id("id_username")
        element.send_keys("")
        element = driver.find_element_by_id("id_password")
        element.send_keys("naval12")
        element.send_keys(Keys.RETURN)
        driver.implicitly_wait(20)
        driver.save_screenshot('screenshot04.png')
        self.assertEqual("Registration complete", self.driver.title)
        driver.close()      


    """" Invalid entries(incorrect password) """

    def test_search_in_python5(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/login/")
        self.assertIn("Log in", driver.title)
        element = driver.find_element_by_id("id_username")
        element.send_keys("naval12")
        element = driver.find_element_by_id("id_password")
        element.send_keys("naval")
        element.send_keys(Keys.RETURN)
        driver.implicitly_wait(20)
        driver.save_screenshot('screenshot05.png')
        self.assertEqual("Registration complete", self.driver.title)
        driver.close()                
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()