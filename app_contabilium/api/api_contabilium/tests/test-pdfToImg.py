import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons

def pdf2File():
    doc = fitz.open(file_path)  # open document
    for page in doc:
        pix = page.get_pixmap()  # render page to an image
        pix.save(f"page_{i}.png")
    

pdf2File()



