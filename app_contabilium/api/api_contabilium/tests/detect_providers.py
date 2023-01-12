import pytesseract
import cv2
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
from pdf2image import convert_from_path

def convert_pdf(pdf_path, save_dir):
    images = convert_from_path(pdf_path, poppler_path = r"C:\Program Files (x86)\poppler-22.12.0\Library\bin")
    name = (os.path.basename(pdf_path))
    for i in range (len(images)):
        images[i].save(f"{save_dir}/"+ f"{name}_{i}" + ".png","PNG")

def readimage(image_path, iy, fy, ix, fx):
    Image = cv2.imread(image_path)
    ROI = Image[iy:fy , ix:fx]
    #cv2.imshow("Facturar A", ROI)
    #cv2.waitKey(0)
    text = (pytesseract.image_to_string(ROI))
    
    
    word = "CUIT:"
    position = text.find(word)
    if position != -1:
        following_text = text[position + len(word): position + len(word) + 14 ]
        print(following_text)
    else:
        word = "C.U.I.T.: " 
        position = text.find(word)
        if position != -1:
            following_text = text[position + len(word): position + len(word) + 13]
            print(following_text)

    
convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/000299_20211110_CA12-00005064  Presmar.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/000299_20211110_CA12-00005064  Presmar.pdf_0.PNG", 60, 330 , 80, 1600)

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Der  NC A-0200-00247974.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Der  NC A-0200-00247974.pdf_0.PNG", 60, 400 , 80, 1600)


