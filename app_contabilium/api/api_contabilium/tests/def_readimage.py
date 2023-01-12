import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def readimage(image_path, iy, fy, ix, fx, ):
    Image = cv2.imread(image_path) #Asignarle una imagen a una variable

    #Para mostrar la imagen, se puede sacar
    #cv2.imshow("Imagen", Image) 
    #cv2.waitKey(0) 

    #ROI
    #Para mostrar la imagen, se puede sacar
    #cv2.imshow("Facturar A", ROI) #Para mostrar la imagen, se puede sacar
    #cv2.waitKey(0) #Para mostrar la imagen, se puede sacar

    #ROI = Image [280:380, 40:200]
    #ROI = Image [215:245 , 900:1050]
    ROI = Image [iy:fy , ix:fx] 
    print (pytesseract.image_to_string(ROI))

#cv2.imwrite(r'C:\Users\estev\Desktop\Prueba Tesseract\ROI1.PNG', ROI) #Guardar una imagen que esta en una variable
#print (pytesseract.image_to_string(r'C:\Users\estev\Desktop\Prueba Tesseract\ROI1.PNG'))

#readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Factura A.PNG")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/000299_20211110_CA12-00005064  Presmar.pdf_0.PNG", 215, 245, 900, 1050)