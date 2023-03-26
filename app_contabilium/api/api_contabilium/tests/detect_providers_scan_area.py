import pytesseract
import cv2
import os
import urllib.request
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from pdf2image import convert_from_path

def convert_pdf(pdf_path, save_dir):
    images = convert_from_path(pdf_path, poppler_path = r"C:\Program Files\poppler-23.01.0\Library\bin")
    name = (os.path.basename(pdf_path))
    for i in range (len(images)):
        images[i].save(f"{save_dir}/"+ f"{name}_{i}" + ".png","PNG")

def readimage(image_path):
    Image = cv2.imread(image_path)
    y = 350
    ROI = Image[60:y, 80:1600]
    text = (pytesseract.image_to_string(ROI))
    contador = 0
    while contador == 0:
         word = "CUIT:"
         position = text.find(word)
         if position != -1:
            following_text = text[position + len(word): position + len(word) + 18]
            contador = contador + 1
         else:
            word = "C.U.I.T." 
            position = text.find(word)
            if position != -1:
                following_text = text[position + len(word): position + len(word) + 18]
                contador = contador + 1
            else:
                y = y + 10
                ROI = Image[60:y , 80:1600]
                text = (pytesseract.image_to_string(ROI))

    numeros = ""
    for caracter in following_text:
        if caracter.isdigit():
            numeros += caracter
    print(numeros)



convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Presmar 000299_20211110_CA12-00005064.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Presmar 000299_20211110_CA12-00005064.pdf_0.PNG")






