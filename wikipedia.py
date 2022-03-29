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
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element_by_link_text("All portals")

# articles.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
sleep(5)
