import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

print (pytesseract.image_to_string(Image.open(r'C:\Users\estev\Desktop\Prueba Tesseract\Factura A.PNG')))