import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Search(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome()
        self.drv.get('https://www.google.com')
    
    def  test_search(self):
         assert 'Google' in self.drv.title
         elem = self.drv.find_element(By.NAME, 'q')
         elem.send_keys('python')
         elem.send_keys(Keys.RETURN)
         assert 'No results found' not in self.drv.page_source
          
    def tearDown(self):
        self.drv.close()
        
if __name__ =='__main__':
    unittest.main()


