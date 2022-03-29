from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#Se descarga e instala el driver que maneja el navegador
chrome_driver_path = r"C:\Users\juanc\Desktop\Desarrollo\Selenium\Selenium\chromedriver.exe"
#Se pasa como el ejecutable para chrome
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Abrir el navegador
driver.get("http://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

first_name.send_keys("Juan")
last_name.send_keys("Pablo")
email.send_keys("juanchito@gmail.com")

first_name.send_keys(Keys.ENTER)
sleep(5)
