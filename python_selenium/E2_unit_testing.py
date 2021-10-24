
#from typeshed import Self
import unittest
#import unittest, time, re, cgi
import os, sys, inspect
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class usando_unittest(unittest.TestCase):
    @classmethod

    #inicializar nuestro driver
    def setUp(self):
        #self.driver = webdriver.Chrome('/Users/fernandoespinoza/Desktop/driver/chromedriver')
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\trihe\Desktop\python\driver\chromedriver.exe")

    def test_buscar(self):
        driver = self.driver
        driver.get("https://www.google.com/")

        self.assertIn("Google", driver.title)
        elemento=driver.find_element_by_name("q")
        elemento.send_keys("selenium")
        elemento.send_keys(Keys.RETURN)

        time.sleep(5)
        assert "No se encontro el elmento:" not in driver.page_source

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":

    unittest.main()  
