import pytesseract
import cv2
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
from pdf2image import convert_from_path

def convert_pdf(pdf_path, save_dir):
    images = convert_from_path(pdf_path, poppler_path = r"C:\Program Files (x86)\poppler-22.12.0\Library\bin")
    name = (os.path.basename(pdf_path))
    for i in range (len(images)):
        images[i].save(f"{save_dir}/"+ f"{name}_{i}" + ".png","PNG")

#def readimage(image_path):
    #Image = cv2.imread(image_path)
    #ROI = Image[60:400 , 80:1600]
    #cv2.imshow("Facturar A", ROI)
    #cv2.waitKey(0)
    #text = (pytesseract.image_to_string(ROI))
    
    
    #word = "CUIT:"
    #position = text.find(word)
    #if position != -1:
        #following_text = text[position + len(word): position + len(word) + 14 ]
        #print(following_text)
    #else:
        #word = "C.U.I.T.: " 
        #position = text.find(word)
        #if position != -1:
            #following_text = text[position + len(word): position + len(word) + 13]
            #print(following_text)

def readimage(image_path):
    Image = cv2.imread(image_path)
    y = 350
    ROI = Image[60:y , 80:1600]
    text = (pytesseract.image_to_string(ROI))
    contador = 0
    while contador == 0:
         word = "CUIT:"
         position = text.find(word)
         if position != -1:
            following_text = text[position + len(word): position + len(word) + 18]
            #print(following_text)
            contador = contador + 1
         else:
            word = "C.U.I.T." 
            position = text.find(word)
            if position != -1:
                following_text = text[position + len(word): position + len(word) + 18]
                #print(following_text)
                contador = contador + 1
            else:
                y = y + 10
                ROI = Image[60:y , 80:1600]
                text = (pytesseract.image_to_string(ROI))

    numeros = ""
    for caracter in following_text:
        if caracter.isdigit():
            numeros += caracter
    print(numeros)
        

                


convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Presmar 000299_20211110_CA12-00005064.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Presmar 000299_20211110_CA12-00005064.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Der  NC A-0200-00247974.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Der  NC A-0200-00247974.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Expoyer  V20220422NSXA0003-00441818.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Expoyer  V20220422NSXA0003-00441818.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Autopiezas de avanzadas  00098-NC-0005-00010443.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Autopiezas de avanzadas  00098-NC-0005-00010443.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Taraborelli FC-A-0108-00026988.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Taraborelli FC-A-0108-00026988.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Friction Lab  NCA0016-00033357.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Friction Lab  NCA0016-00033357.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Cromosol  comprobante-Cromosol-0018-00000476.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Cromosol  comprobante-Cromosol-0018-00000476.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Getres  FACTURA LAMPERTI 11945.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Getres  FACTURA LAMPERTI 11945.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Icepar  72891_115107-0001-0015-CEA-0000106920.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Icepar  72891_115107-0001-0015-CEA-0000106920.pdf_0.PNG")

#No anduvo convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/New Clevers FACA0000200021361.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
#No anduvo readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/New Clevers FACA0000200021361.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/NC  A0010-00002302  Ar accesorios.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/NC  A0010-00002302  Ar accesorios.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Rural Santa Fe  0101012795.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Rural Santa Fe  0101012795.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Taranto  FACTURA-A-0101-00325624.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Taranto  FACTURA-A-0101-00325624.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/V54  20220601FACFE_FAC_AA0002-00011275.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/V54  20220601FACFE_FAC_AA0002-00011275.pdf_0.PNG")

convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Warnes Plaza  FA000200070000.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Warnes Plaza  FA000200070000.pdf_0.PNG")





