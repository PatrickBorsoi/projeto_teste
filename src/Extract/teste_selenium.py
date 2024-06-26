#%%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import requests
# Configuração do WebDriver do Chrome
options = ChromeOptions()
# options.add_argument("--headless")  # Execução em modo headless (sem interface gráfica)

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

#%%
# URL a ser acessada
url = "https://www.ioerj.com.br/portal/modules/conteudoonline/mostra_edicao.php?session=VVRCU1FsRlZUa0pPVkUxMFVXcGplRTFUTURCU2FrcEdURlZKZWxGVVJYUlJWR014VGtSb1JFMHdTVEZOVkZaQ1RWUmplRTlVVFRKT1ZGRjVUa0U5UFE9PQ=="
#%%
try:
    # Abrir a página
    driver.get(url)
    # driver.implicitly_wait(10)
    # Pegar o conteúdo do iframe que contém o PDF
    # html = driver.page_source
    # soup = BeautifulSoup(html, "html.parser")


    # Fechar o navegador
    # driver.quit()

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    driver.quit()

# %%
