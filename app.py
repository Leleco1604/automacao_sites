from selenium import webdriver
from selenium.webdriver.common.by import By #acessar informações do site 
import openpyxl


# acessar site https://www.novaliderinformatica.com.br
driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')

# extrair todos os titulos
titulos = driver.find_element(By.XPATH, "//a[@class='nome-produto']")
# estrair todos os preços
precos = driver.find_element(By.XPATH, "//strong[@class='preco-promocional']")
# inserir tudo em uma planilha 
#zip: faz com que o o for so percorra itens que estão nas duas listas
for titulo, preco in zip(titulos, precos): 
    pass 

