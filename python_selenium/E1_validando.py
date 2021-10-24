from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\trihe\Desktop\python\driver\chromedriver.exe")

#driver = webdriver.Chrome('/Users/fernandoespinoza/Desktop/driver/chromedriver')

driver.get("https://www.selenium.dev/documentation/")
driver.close