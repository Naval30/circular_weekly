"""Test to register with a valid username, email id and password"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()


    """Valid entries"""

    def test_search_in_python1(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/register/")
        self.assertIn("Sign up", driver.title)
        element = driver.find_element_by_id("id_username")
        element.send_keys("Tom")
        element = driver.find_element_by_id("id_email")
        element.send_keys("navalnain@yahoo.co.in")
        element = driver.find_element_by_id("id_password1")
        element.send_keys("Tomadd")
        element = driver.find_element_by_id("id_password2")
        element.send_keys("Tomadd")
        element.send_keys(Keys.RETURN)
        driver.implicitly_wait(20)
        driver.save_screenshot('screenshot1.png')
        self.assertEqual("Registration complete", self.driver.title)
        driver.close()


    """Invalid entries(space in username)"""

    def test_search_in_python2(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/register/")
        self.assertIn("Sign up", driver.title)
        element = driver.find_element_by_id("id_username")
        element.send_keys("Harry Backus")
        element = driver.find_element_by_id("id_email")
        element.send_keys("navalnain@yahoo.co.in")
        element = driver.find_element_by_id("id_password1")
        element.send_keys("Harry")
        element = driver.find_element_by_id("id_password2")
        element.send_keys("Harry")
        element.send_keys(Keys.RETURN)
        driver.implicitly_wait(20)
        driver.save_screenshot('screenshot2.png')
        self.assertEqual("Registration complete", self.driver.title)
        driver.close()    


    """Valid entries"""

    def test_search_in_python3(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/register/")
        self.assertIn("Sign up", driver.title)
        element = driver.find_element_by_id("id_username")
        element.send_keys("Ferrari")
        element = driver.find_element_by_id("id_email")
        element.send_keys("navalnain@yahoo.co.in")
        element = driver.find_element_by_id("id_password1")
        element.send_keys("Tom add")
        element = driver.find_element_by_id("id_password2")
        element.send_keys("Tom add")
        element.send_keys(Keys.RETURN)
        driver.implicitly_wait(20)
        driver.save_screenshot('screenshot3.png')
        self.assertEqual("Registration complete", self.driver.title)
        driver.close()    


    """Invalid entries(Invalid email)"""

    def test_search_in_python4(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/register/")
        self.assertIn("Sign up", driver.title)
        element = driver.find_element_by_id("id_username")
        element.send_keys("TomHanks")
        element = driver.find_element_by_id("id_email")
        element.send_keys("TomHanks")
        element = driver.find_element_by_id("id_password1")
        element.send_keys("Tomadd")
        element = driver.find_element_by_id("id_password2")
        element.send_keys("Tomadd")
        element.send_keys(Keys.RETURN)
        driver.implicitly_wait(20)
        driver.save_screenshot('screenshot4.png')
        self.assertEqual("Registration complete", self.driver.title)
        driver.close()  
        

    """Invalid entries(different passwords)"""

    def test_search_in_python5(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/register/")
        self.assertIn("Sign up", driver.title)
        element = driver.find_element_by_id("id_username")
        element.send_keys("Beth")
        element = driver.find_element_by_id("id_email")
        element.send_keys("navalnain@yahoo.co.in")
        element = driver.find_element_by_id("id_password1")
        element.send_keys("Beth")
        element = driver.find_element_by_id("id_password2")
        element.send_keys("LBeth")
        element.send_keys(Keys.RETURN)
        driver.implicitly_wait(20)
        driver.save_screenshot('screenshot5.png')
        self.assertEqual("Registration complete", self.driver.title)
        driver.close()      
        

    """Valid entries"""    

    def test_search_in_python6(self):
        driver = self.driver
        driver.get("http://weekly-circular.herokuapp.com/accounts/register/")
        self.assertIn("Sign up", driver.title)
        element = driver.find_element_by_id("id_username")
        element.send_keys("Tom")
        element = driver.find_element_by_id("id_email")
        element.send_keys("navalnain@yahoo.co.in")
        element = driver.find_element_by_id("id_password1")
        element.send_keys("Tomadd")
        element = driver.find_element_by_id("id_password2")
        element.send_keys("Tomadd")
        element.send_keys(Keys.RETURN)
        driver.save_screenshot('screenshot6.png')
        driver.implicitly_wait(20)
        self.assertEqual("Registration complete", self.driver.title)
        driver.close()    


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()