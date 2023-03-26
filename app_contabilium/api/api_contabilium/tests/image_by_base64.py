import pytesseract
import cv2
import base64
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def readimage():
    codigo_base64 = ""
    imagen_bytes = base64.b64decode(codigo_base64)
    imagen_numpy = np.frombuffer(imagen_bytes, np.uint8)
    Image = cv2.imdecode(imagen_numpy, cv2.IMREAD_COLOR)
    text = (pytesseract.image_to_string(Image))
    print (text)

readimage()
