from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class pesquisa: #classe acessa o google e realiza uma pesquisa
    path = "C:\chromedriver.exe" #instancia o caminho ate o local onde esta o arquivo do driver
    driver = webdriver.Chrome(path) #chama o driver
   
      

    def chamarNavegador(self): #recebe como argumento as variveis da propria classe
       self.driver.get("http://www.google.com.br") #chama driver para acessar o site
       time.sleep(2)
    
    def inserirDadosPesquisa(self):
        placeholderBusca = self.driver.find_element_by_name("q")        
        botaoBusca = self.driver.find_element_by_name("btnK")
        placeholderBusca.send_keys("IGN")
        time.sleep(2)
        botaoBusca.click()
       # elemento.clear() #limpa o que foi escrito no placeholder
        

    


teste = pesquisa()
teste.chamarNavegador()
teste.inserirDadosPesquisa()


