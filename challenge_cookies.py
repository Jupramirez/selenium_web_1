from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Se descarga e instala el driver que maneja el navegador
chrome_driver_path = r"C:\Users\juanc\Desktop\Desarrollo\Selenium\Selenium\chromedriver.exe"
#Se pasa como el ejecutable para chrome
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Abrir el navegador
driver.get("http://orteil.dashnet.org/experiments/cookie/")


#dar click en la galleta

cookie = driver.find_element_by_id("cookie")

time_store = time.time() + 10
timeout = time.time() + 60*2


#Obtener los id de los divs para luego seleccionarlos
items_id = driver.find_elements_by_css_selector("#store div")
item = [item.get_attribute("id") for item in items_id]

while True:

    cookie.click()

    #Hacer cada 5 segundos
    if time.time() > time_store:
        #Obtener los precios de los poderes
        items_prices = driver.find_elements_by_css_selector("#store b")
        prices = []

        #Dejando la lista de precios
        for price in items_prices:
            element_text = price.text
            if element_text != "":
                prices.append(int(element_text.split("-")[1].strip().replace(",", "")))
        
        #haciendo un diccionario con los id y precios
        total_powers = {}
        for i in range(len(prices)):
            total_powers[prices[i]] = item[i]

        #Obtener el dinero actual
        money = driver.find_element_by_id("money").text
        money = int(money)

        #diccionario de poderes disponibles
        afford_powers = {}
        for cost, id in total_powers.items():
            if cost < money:
                afford_powers[cost] = id
        
        #Obtener el maximo de los disponible
        max_cost = max(afford_powers)
        to_click_id = afford_powers[max_cost]


        #Dar click sobre el poder maximo
        driver.find_element_by_id(to_click_id).click()

        #add 5 segundos al reloj
        time_store = time.time() + 10

    if time.time() > timeout:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break





