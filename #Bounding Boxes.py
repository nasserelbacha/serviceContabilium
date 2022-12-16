#Bounding Boxes
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#Preprocessing para identificar estructuras en las imagenes
image = cv2.imread((r'C:\Users\estev\Desktop\Prueba Tesseract\Factura A.PNG'))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(r'C:\Users\estev\Desktop\Prueba Tesseract\Factura A gray.png', gray)
blur = cv2.GaussianBlur(gray, (7,7), 0)
cv2.imwrite(r'C:\Users\estev\Desktop\Prueba Tesseract\Factura A blur.png', blur)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imwrite(r'C:\Users\estev\Desktop\Prueba Tesseract\Factura A thresh.png', thresh)
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3,13))
cv2.imwrite(r'C:\Users\estev\Desktop\Prueba Tesseract\Factura A kernal.png', kernal)
dilate = cv2.dilate(thresh, kernal, iterations=1)
cv2.imwrite(r'C:\Users\estev\Desktop\Prueba Tesseract\Factura A dilate.png', dilate)

cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cents[1]
cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])
for c in cnts:
    x, y, w, h  = cv2.boundingRect(c)
    if h > 50 and w > 50:
        cv2.rectangle(image, (x,y), (x+w, y+h), (36,255,12), 2)
cv2.imwrite(r'C:\Users\estev\Desktop\Prueba Tesseract\Factura A box.png', image)