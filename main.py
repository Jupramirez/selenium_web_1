from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

#Se descarga e instala el driver que maneja el navegador
chrome_driver_path = r"C:\Users\juanc\Desktop\Desarrollo\Selenium\Selenium\chromedriver.exe"
#Se pasa como el ejecutable para chrome
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Abrir el navegador
driver.get("https://www.python.org/")

# Sacar elemento por el nombre
search_bar = driver.find_element(By.NAME, value = "q")
#Sacar elemento por la clase
logo = driver.find_element_by_class_name("python-logo")
#Sacar elemento por el selector css
documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
#elemento por la ruta xpath
status_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[4]/a')

print(status_link.text)
print(documentation_link.text)
print(logo.size)
#Obtener el atributo especifico
print(search_bar.get_attribute("placeholder"))
