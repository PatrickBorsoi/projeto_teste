#%%
import requests
import fitz  # PyMuPDF


#%%
# URL do PDF
url = 'https://www.ioerj.com.br/portal/modules/conteudoonline/mostra_edicao.php?session=VFVSR1JrNVVUa1JQUkZGMFRUQlJNVTFETURCUFJFNURURlZKTlU1cVZYUlNhMGwzVDFSTk5WSnFXa1JPUlZreFRWUmplRTlFV1RKUFZGRTFUMEU5UFE9PQ=='

# Fazendo a requisição GET
response = requests.get(url)
#%%
# Certifique-se de que a resposta foi bem-sucedida
if response.status_code == 200:
    # Carrega o PDF na memória
    pdf_data = response.content

    # Abre o PDF usando PyMuPDF
    pdf_document = fitz.open(stream=pdf_data, filetype="pdf")

    # Itera sobre cada página e extrai o texto
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()
        print(f"Página {page_num + 1}:\n{text}\n")
else:
    print(f"Falha ao acessar o PDF: Status code {response.status_code}")



#%%
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configurar tentativas de reconexão e timeouts
retry_strategy = Retry(
    total=3,  # Número de tentativas
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "OPTIONS"],  # Substitua method_whitelist por allowed_methods
    backoff_factor=1
)

adapter = HTTPAdapter(max_retries=retry_strategy)

http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

url = "https://www.ioerj.com.br/portal/modules/conteudoonline/mostra_edicao.php?session=VG10Tk0wNVZUVEpTUlZWMFRVVlpOVTU1TURCUmEwMDBURlJuZVZKcVkzUlNWVkpHVG1wR1EwOVVRVEpQVkVKSFRWUmplRTlFU1RSTlZFVTBUVUU5UFE9PQ=="

try:
    response = http.get(url, timeout=10)  # Ajuste o timeout conforme necessário
    response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP ruins
    print(response.text)  # Ou processar a resposta conforme necessário
except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro: {e}")
# %%
import http.client

conn = http.client.HTTPSConnection("www.ioerj.com.br")
conn.request("GET", "/portal/modules/conteudoonline/mostra_edicao.php?session=VG10Tk0wNVZUVEpTUlZWMFRVVlpOVTU1TURCUmEwMDBURlJuZVZKcVkzUlNWVkpHVG1wR1EwOVVRVEpQVkVKSFRWUmplRTlFU1RSTlZFVTBUVUU5UFE9PQ==")
response = conn.getresponse()

print(response.status, response.reason)
data = response.read()
print(data)
conn.close()

# %%
