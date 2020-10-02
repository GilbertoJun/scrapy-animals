import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json


url = "https://www.procure1amigo.com.br/"

option = Options()
option.headless = False
driver = webdriver.Firefox(options=option)

driver.get(url)

time.sleep(3)

# # ADICIONANDO E-MAIL E SENHA - FACEBOOK
# driver.find_element_by_id("email").send_keys(emailUsuario)
# driver.find_element_by_id("pass").send_keys(senhaUsuario)

# REALIZA O LOGIN
# driver.find_element_by_xpath("//button[@name='login']").click()

# # VAI ATE A AREA COMERCIAL
# time.sleep(1)
# driver.find_element_by_xpath("//a[@aria-label='Marketplace']").click()

# time.sleep(3)

# driver.quit()
animais = driver.find_element_by_xpath("//div[@class='animais-home']//a[@class='']")
print(animais)


