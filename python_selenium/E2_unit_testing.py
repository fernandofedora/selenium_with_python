#from _typeshed import Self
import unittest
import unittest, time, re, cgi
import os, sys, inspect
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class testcaseA(unittest.TestCase):
    #inicializar nuestro driver
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/fernandoespinoza/Desktop/driver/chromedriver')

    def test_buscar(self):
        driver =self.driver
        driver.get("https://www.google.com/")
        self.assertIn("google", driver.title)
        elemnto=driver.find_element_by_name("q")
        elemnto.send_keys("selenium")
        elemnto.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontro el elmento:" not in driver.page_source

    def tearDown(self) -> None:
        return super().tearDown()

    if __name__ == '_main_':
        unittest.main()   
     
    
    