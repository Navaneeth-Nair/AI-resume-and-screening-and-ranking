import io
import docx2txt as text
import fitz  # PyMuPDF

def extract_text(file):
    file_bytes = file.read()  # Read file bytes
    file_name = file.name.lower()

    if file_name.endswith(".pdf"):
        # Open PDF from memory stream
        with fitz.open(stream=io.BytesIO(file_bytes), filetype="pdf") as pdf_doc:
            txt = "\n".join([page.get_text() for page in pdf_doc])

    elif file_name.endswith(".docx"):
        txt = text.process(io.BytesIO(file_bytes))

    else:
        txt = "Unsupported file format"

    return txt.strip() if txt else "No text extracted"
