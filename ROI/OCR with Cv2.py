import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


def readimage():
    Image = cv2.imread((r'C:\Users\estev\Desktop\Prueba Tesseract\Codigos\serviceContabilium\Factura A.PNG')) #Asignarle una imagen a una variable

    #Para mostrar la imagen, se puede sacar
    #cv2.imshow("Imagen", Image) 
    #cv2.waitKey(0) 

    #ROI
    #Para mostrar la imagen, se puede sacar
    #cv2.imshow("Facturar A", ROI) #Para mostrar la imagen, se puede sacar
    #cv2.waitKey(0) #Para mostrar la imagen, se puede sacar

    facturar = Image [280:380, 40:200] 
    print (pytesseract.image_to_string(facturar))
    enviar = Image [280:380 , 290:425]
    print (pytesseract.image_to_string(enviar))
    fecha = Image[200:225, 620:710]
    print (pytesseract.image_to_string(fecha))
    subtotal = Image [573:601, 651:711]
    print (pytesseract.image_to_string(subtotal))
    iva = Image [610:630, 650:710]
    print (pytesseract.image_to_string(iva))
    total = Image [655:700, 570:670]
    print (pytesseract.image_to_string(total))
    nfactura = Image [170:197, 640:710]
    print (pytesseract.image_to_string(nfactura))
    
    

#cv2.imwrite(r'C:\Users\estev\Desktop\Prueba Tesseract\ROI1.PNG', ROI) #Guardar una imagen que esta en una variable
#print (pytesseract.image_to_string(r'C:\Users\estev\Desktop\Prueba Tesseract\ROI1.PNG'))

def main():
    readimage()

main()

coordinates = [] 
def shape_selection(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: 
        coordinates = [(x, y)] 
    elif event == cv2.EVENT_LBUTTONUP: 
        coordinates.append((x, y)) 
    cv2.rectangle(image, coordinates[0], coordinates[1], (0,255,255), 2) 
    cv2.imshow("image", image) 