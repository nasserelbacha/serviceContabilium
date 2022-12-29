#OCR with Cv2
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#Open Image
Image = cv2.imread((r'C:\Users\estev\Desktop\Prueba Tesseract\Factura A.PNG')) #Asignarle una imagen a una variable
cv2.imshow("Imagen", Image) #Para mostrar la imagen, se puede sacar
cv2.waitKey(0) #Para mostrar la imagen, se puede sacar

#ROI
ROI = Image [280:380, 40:200] 
cv2.imshow("Facturar A", ROI) #Para mostrar la imagen, se puede sacar
cv2.waitKey(0) #Para mostrar la imagen, se puede sacar
cv2.imwrite(r'C:\Users\estev\Desktop\Prueba Tesseract\ROI1.PNG', ROI) #Guardar una imagen que esta en una variable (Lugar donde se guarda, variable)

print (pytesseract.image_to_string(r'C:\Users\estev\Desktop\Prueba Tesseract\ROI1.PNG'))
