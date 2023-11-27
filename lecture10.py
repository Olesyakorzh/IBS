from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://google.com/ncr')
        time.sleep(1)
        
    def test_search(self):
        assert 'Google' in self.driver.title
        elem = self.driver.find_element(By.NAME, 'q')
        elem.send_keys('selenide')
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        ### Ищем первый результат
        elem = self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/div/div/div/cite')
        assert elem.text == 'https://selenide.org'
        print("Элемент найден")
        result = elem.text
        elem = self.driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a' )
        elem.click()
        elem = self.driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[2]/div[1]/div')
        assert 'ru.selenide.org' in elem.text
        print("Изображение подходит")
        
        elem = self.driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]')
        elem.click()
        
        ### В разделе Картинки ссылка меняется на ru.selenide.org, совпадение невозможно.
        assert self.driver.find_element(By.XPATH, '//*[@id="APjFqb"]').text == result, "Ссылки не совпадают"
        print("Ссылки не совпадают")       
    
    def tearDown(self):
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()  
        