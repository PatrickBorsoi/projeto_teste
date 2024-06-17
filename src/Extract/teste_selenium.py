#%%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do WebDriver do Chrome
options = ChromeOptions()
# options.add_argument("--headless")  # Execução em modo headless (sem interface gráfica)

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL a ser acessada
url = "https://www.ioerj.com.br/portal/modules/conteudoonline/mostra_edicao.php?session=VG10Tk0wNVZUVEpTUlZWMFRVVlpOVTU1TURCUmEwMDBURlJuZVZKcVkzUlNWVkpHVG1wR1EwOVVRVEpQVkVKSFRWUmplRTlFU1RSTlZFVTBUVUU5UFE9PQ=="

try:
    # Abrir a página
    driver.get(url)
    time.sleep(5)  # Espera um tempo suficiente para o conteúdo ser carregado (pode ajustar conforme necessário)

    # Pegar o conteúdo do iframe que contém o PDF
    iframe = driver.find_element_by_xpath("//*[@id='next']")
    # driver.switch_to.frame(iframe)  # Mudar para o contexto do iframe

    # # Obter o link do PDF dentro do iframe
    # pdf_element = driver.find_element_by_tag_name("embed")
    # pdf_src = pdf_element.get_attribute("src")

    # # Imprimir o link do PDF (opcional)
    # print("Link do PDF:", pdf_src)

    # Fechar o navegador
    driver.quit()

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    driver.quit()

# %%
