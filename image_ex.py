import PyPDF2
import openai
from main import apikey
path = ""
def extract(path):
    text = ""
    with open(path, 'rb') as pdf_file:
        pdf_read = PyPDF2.PdfFileReader(pdf_file)
        for page in pdf_read.pages():
            text += page.extract_text()
    return text


pdf_path = 'Users/admin/Desktop/rpa folder/Certificate.pdf'
pdf_text = extract(path)


prompt = f'What is the summary in pdf about:\n{pdf_text}\n'

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=50,
    temperature=0.7
)

print(response.choices[0].text)