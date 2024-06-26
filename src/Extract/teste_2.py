#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
import fitz  # PyMuPDF
import time
#%%
# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser
driver.get('https://www.ioerj.com.br/portal/modules/conteudoonline/mostra_edicao.php?session=VVRCU1FsRlZUa0pPVkUxMFVXcGplRTFUTURCU2FrcEdURlZKZWxGVVJYUlJWR014VGtSb1JFMHdTVEZOVkZaQ1RWUmplRTlVVFRKT1ZGRjVUa0U5UFE9PQ==')

# Wait for the page to load and find the PDF links (adjust the sleep time as needed)
# time.sleep(5)
# pdf_link_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]")
# pdf_urls = [element.get_attribute('href') for element in pdf_link_elements]

# # Function to extract text from PDF URL using PyMuPDF
# def extract_text_from_pdf_url(pdf_url):
#     text = ""
#     pdf_document = fitz.open(pdf_url)
#     for page_num in range(len(pdf_document)):CD
#         page = pdf_document.load_page(page_num)
#         text += page.get_text()
#     return text

# # Example usage
# for pdf_url in pdf_urls:
#     print(f"Extracting text from: {pdf_url}")
#     pdf_text = extract_text_from_pdf_url(pdf_url)
#     print(f"Text extracted from {pdf_url}:\n", pdf_text)

# # Close the Selenium WebDriver
# driver.quit()
