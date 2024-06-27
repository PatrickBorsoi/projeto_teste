from PyPDF2 import PdfReader

# Caminho para o arquivo PDF
pdf_path = 'C:/Users/Patrick/Desktop/workspace/projeto_diario_oficial/IOERJTraceableFile667ceedba6a4d.pdf'

# Abrir o arquivo PDF
reader = PdfReader(pdf_path)
number_of_pages = len(reader.pages)
all_text = ""

# Iterar por todas as páginas e extrair o texto
for page_number in range(number_of_pages):
    page = reader.pages[page_number]
    text = page.extract_text()
    all_text += text if text else ""

print(all_text)
