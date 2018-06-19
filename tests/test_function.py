import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time; 

class Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search(self):
        driver = self.driver
        driver.get("https://leisuretime.herokuapp.com/")
        
        elem = driver.find_element_by_id("id_description__icontains")
        elem.send_keys("festa")
        
        time.sleep(2)
        ok = driver.find_element_by_id("submitsearch").click()
      

        elem2 = driver.find_element_by_id("id_description__icontains")
        elem2.send_keys("meaño")
        time.sleep(2)
        ok2 = driver.find_element_by_id("submitsearch").click()
    

        elem3 = driver.find_element_by_id("id_description__icontains")
        elem3.send_keys("cambados")
        time.sleep(2)
        ok3 = driver.find_element_by_id("submitsearch").click()
      
        time.sleep(2)
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()