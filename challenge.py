from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

#Se descarga e instala el driver que maneja el navegador
chrome_driver_path = r"C:\Users\juanc\Desktop\Desarrollo\Selenium\Selenium\chromedriver.exe"
#Se pasa como el ejecutable para chrome
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Abrir el navegador
driver.get("https://www.python.org/")

# Se puede obtener por selectores de clase, id, tag
upcoming_time_events = driver.find_elements_by_css_selector(".event-widget time")
upcoming_events = driver.find_elements_by_css_selector(".event-widget a")

print(upcoming_time_events[0].text)

dic_events = {}
 # rellenamos un diccionario
for i in range(5):
    dic_events[i] = {
        'time': upcoming_time_events[i].text,
        'name': upcoming_events[i].text
    }