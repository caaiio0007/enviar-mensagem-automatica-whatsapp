from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

#esperar carregar

# whats já carregou
import pandas as pd

tabela = pd.read_excel("Enviar.xlsx")
import urllib
import time

for linha in tabela.index:
    # enviar mensagem para a pessoa
    nome =  tabela.loc[linha, "Pessoa"]
    mensagem = tabela.loc[linha, "Mensagem"]
    telefone = tabela.loc[linha, "Número"]

    texto = mensagem.replace("fulano", nome)
    texto = urllib.parse.quote(texto)
   
    # enviar a mensagem
    link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"

    navegador.get(link)
    # esperar a tela carregar
    while len(navegador.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
    time.sleep(2) #garantia de que carregou tudo
    # enviar a mensagem
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    time.sleep(2)