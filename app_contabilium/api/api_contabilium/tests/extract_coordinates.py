import cv2

image = cv2.imread(r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Presmar 000299_20211110_CA12-00005064.pdf_1.png")
coordinates = [] 

def shape_selection(event, x, y, flags, param):     
    global coordinates 
    if event == cv2.EVENT_LBUTTONDOWN: # Storing the (x1,y1) coordinates when left mouse button is pressed  
        coordinates = [(x, y)] 
    elif event == cv2.EVENT_LBUTTONUP: # Storing the (x2,y2) coordinates when the left mouse button is released and make a rectangle on the selected region
        coordinates.append((x, y)) 
        cv2.rectangle(image, coordinates[0], coordinates[1], (0,0,255), 2)

cv2.namedWindow('image')
cv2.setMouseCallback('image',shape_selection)

while(True):
    cv2.imshow('image',image)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

print(f'Coordenadas de selección: x1={coordinates[0]}, y1={coordinates[1]}')
cv2.destroyAllWindows() 