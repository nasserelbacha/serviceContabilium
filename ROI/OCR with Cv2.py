import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def readimage():
    Image = cv2.imread((r'C:\Users\estev\Desktop\Prueba Tesseract\Factura A.PNG')) #Asignarle una imagen a una variable

    #Para mostrar la imagen, se puede sacar
    #cv2.imshow("Imagen", Image) 
    #cv2.waitKey(0) 

    #ROI
    #Para mostrar la imagen, se puede sacar
    #cv2.imshow("Facturar A", ROI) #Para mostrar la imagen, se puede sacar
    #cv2.waitKey(0) #Para mostrar la imagen, se puede sacar

    ROI = Image [280:380, 40:200] 
    print (pytesseract.image_to_string(ROI))

#cv2.imwrite(r'C:\Users\estev\Desktop\Prueba Tesseract\ROI1.PNG', ROI) #Guardar una imagen que esta en una variable
#print (pytesseract.image_to_string(r'C:\Users\estev\Desktop\Prueba Tesseract\ROI1.PNG'))

def main():
    readimage()

main()