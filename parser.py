import io
import docx2txt as text
import pymupdf as pdf

def extract_text(file):
    file_bytes = file.read()
    
    if file.name.lower().endswith(".pdf"):
        pdfdata = pdf.open(file, filetype='txt')
        txt = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file.name.lower().endswith(".docx"):
        txt = text.process(io.BytesIO(file_bytes))
    else:
        txt = ""

    return txt.strip() if txt else "No text extracted"