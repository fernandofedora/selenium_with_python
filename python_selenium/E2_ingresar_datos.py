from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittes


driver = webdriver.Chrome(executable_path=r"C:\Users\trihe\Desktop\python\driver\chromedriver.exe")
driver.get("https://www.gmail.com")


usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("noelonassis@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_name("password")
clave.send_keys("nami123")
clave.send_keys(Keys.ENTER)



