import pytesseract
import cv2
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
from pdf2image import convert_from_path
from PIL import Image


def convert_pdf(pdf_path, save_dir):
    images = convert_from_path(pdf_path, poppler_path = r"C:\Program Files (x86)\poppler-22.12.0\Library\bin", fmt="jpeg" )
    name = (os.path.basename(pdf_path))
    for i in range (len(images)):
        images[i].save(f"{save_dir}/"+ f"{name}_{i}" + ".png","PNG")

def readimage(image_path, iy, fy, ix, fx):
    Image = cv2.imread(image_path)
    ROI = Image[iy:fy , ix:fx] 
    print (pytesseract.image_to_string(ROI))  

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/000299_20211110_CA12-00005064  Presmar.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/000299_20211110_CA12-00005064  Presmar.pdf_0.PNG", 215, 245, 900, 1050)

#"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/000299_20211110_CA12-00005064  Presmar.pdf"