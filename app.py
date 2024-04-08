from selenium import webdriver
from selenium.webdriver.common.by import By #acessar informações do site 
import openpyxl


# acessar site https://www.novaliderinformatica.com.br
driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')

titulos = driver.find_element(By.XPATH, "//a[@class='nome-produto']")
preco = driver.find_element(By.XPATH, "")

# extrair todos os titulos
# estrair todos os preços
# inserir tudo em uma planilha 

