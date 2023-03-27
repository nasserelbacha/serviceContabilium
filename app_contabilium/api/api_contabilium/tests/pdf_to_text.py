import pytesseract
import cv2
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
from pdf2image import convert_from_path


def convert_pdf(pdf_path, save_dir):
    images = convert_from_path(pdf_path, poppler_path = r"C:\Program Files\poppler-23.01.0\Library\bin", fmt="jpeg" )
    name = (os.path.basename(pdf_path))
    for i in range (len(images)):
        images[i].save(f"{save_dir}/"+ f"{name}_{i}" + ".png","PNG")

cordinates = [{215:245 , 900:1050}]
i=0
ROI=0
def readimage(image_path, iy, fy, ix, fx):
    Image = cv2.imread(image_path)
    while ROI == 0:
    ROI = Image[cordinates{i}] 
    print (pytesseract.image_to_string(ROI)) 
    i+1 

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/000299_20211110_CA12-00005064  Presmar.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/000299_20211110_CA12-00005064  Presmar.pdf_0.PNG", 215, 245, 900, 1050)

#"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/000299_20211110_CA12-00005064  Presmar.pdf"
