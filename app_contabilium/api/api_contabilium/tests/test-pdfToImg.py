import PyPDF2

def pdf2File():
    pdfFileObj = open('test_factura.pdf', 'rb')
    pdf = PyPDF2.PdfReader(pdfFileObj)
    print(pdf.pages)
    # creating a page object
    pageObj = pdf.pages[0]
    text = pageObj.extract_text()
    file1 = open("1","a")
    file1.writelines(text)
    pdfFileObj.close()
    

pdf2File()
