import pytesseract
import cv2
import os
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# from pdf2image import convert_from_path
import pypdfium2 as pdfium


def convert_pdf(pdf_path, save_dir):
    pdf = pdfium.PdfDocument("test_factura.pdf")
    n_pages = len(pdf)
    for page_number in range(n_pages):
        page = pdf.get_page(page_number)
        pil_image = page.render_topil(
            scale=1,
            rotation=0,
            crop=(0, 0, 0, 0),
            # colour=(255, 255, 255, 255),
            # annotations=True,
            greyscale=False,
            optimise_mode=pdfium.OptimiseMode.NONE,
        )       
        pil_image.save(f"image_{page_number+1}.png")
def readimage(image_path):
    Image = cv2.imread(image_path)
    # y = "60:350"
    # y = y.split(":")
    # y1 = int(y[0])
    # y2 = int(y[1])
    y = 350
    ROI = Image[60:y, 80:1600]
    text = (pytesseract.image_to_string(ROI))
    contador = 0
    print(text)
    while contador == 0:
         word = "CUIT:"
         position = text.find(word)
         if position != -1:
            following_text = text[position + len(word): position + len(word) + 18]
            print(following_text)
            contador = contador + 1
         else:
            word = "C.U.I.T." 
            position = text.find(word)
            if position != -1:
                following_text = text[position + len(word): position + len(word) + 18]
                print(following_text)
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
        

readimage("image_1.png")                            
# convert_pdf('./facturas/Presmar 000299_20211110_CA12-00005064.pdf', 'api/api_contabilium/tests/facturas/Presmar 000299_20211110_CA12-00005064.pdf_0.PNG"')
# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Presmar 000299_20211110_CA12-00005064.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Presmar 000299_20211110_CA12-00005064.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Der  NC A-0200-00247974.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Der  NC A-0200-00247974.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Expoyer  V20220422NSXA0003-00441818.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Expoyer  V20220422NSXA0003-00441818.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Autopiezas de avanzadas  00098-NC-0005-00010443.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Autopiezas de avanzadas  00098-NC-0005-00010443.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Taraborelli FC-A-0108-00026988.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Taraborelli FC-A-0108-00026988.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Friction Lab  NCA0016-00033357.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Friction Lab  NCA0016-00033357.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Cromosol  comprobante-Cromosol-0018-00000476.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Cromosol  comprobante-Cromosol-0018-00000476.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Getres  FACTURA LAMPERTI 11945.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Getres  FACTURA LAMPERTI 11945.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Icepar  72891_115107-0001-0015-CEA-0000106920.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Icepar  72891_115107-0001-0015-CEA-0000106920.pdf_0.PNG")

# # #No anduvo convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/New Clevers FACA0000200021361.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# # #No anduvo readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/New Clevers FACA0000200021361.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/NC  A0010-00002302  Ar accesorios.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/NC  A0010-00002302  Ar accesorios.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Rural Santa Fe  0101012795.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Rural Santa Fe  0101012795.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Taranto  FACTURA-A-0101-00325624.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Taranto  FACTURA-A-0101-00325624.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/V54  20220601FACFE_FAC_AA0002-00011275.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/V54  20220601FACFE_FAC_AA0002-00011275.pdf_0.PNG")

# convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Warnes Plaza  FA000200070000.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")
# readimage (r"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/Warnes Plaza  FA000200070000.pdf_0.PNG")





