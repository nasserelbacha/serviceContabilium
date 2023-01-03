import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

image = cv2.imread(r'C:\Users\estev\Desktop\Prueba Tesseract\Codigos\serviceContabilium\Factura B1.PNG')

coordinates = [] 
  
def shape_selection(event, x, y, flags, param): 
    global coordinates 
    if event == cv2.EVENT_LBUTTONDOWN: 
        coordinates = [(x, y)] 
    elif event == cv2.EVENT_LBUTTONUP: 
        coordinates.append((x, y)) 
        cv2.rectangle(image, coordinates[0], coordinates[1], (0,255,255), 2) 
        cv2.imshow("image", image)   
image_copy = image.copy()
cv2.namedWindow("image") 
cv2.setMouseCallback("image", shape_selection)  
while True: 
    cv2.imshow("image", image) 
    key = cv2.waitKey(1) & 0xFF
    if key==13: # If 'enter' is pressed, apply OCR
        break
    if key == ord("c"): # Clear the selection when 'c' is pressed 
        image = image_copy.copy()  
if len(coordinates) == 2: 
    image_roi = image_copy[coordinates[0][1]:coordinates[1][1], 
                               coordinates[0][0]:coordinates[1][0]] 
    cv2.imshow("Selected Region of Interest - Press any key to proceed", image_roi) 
    cv2.waitKey(0)  

cv2.destroyAllWindows()  
    
text = pytesseract.image_to_string(image_roi)
print("The text in the selected region is as follows:")
print(text)