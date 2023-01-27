from pdf2image import convert_from_path
import os

def convert_pdf(pdf_path, save_dir, res=400):
    images = convert_from_path(pdf_path, poppler_path = r"C:\Program Files (x86)\poppler-22.12.0\Library\bin")
    #name_with_extension = pdf_path.rsplit("/")[-1]
    #name = name_with_extension.rsplit(".")[0]
    name = (os.path.basename(pdf_path))
    for i in range (len(images)):
        images[i].save(f"{save_dir}/"+ f"{name}_{i}" + ".png","PNG")
    
convert_pdf("C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/000299_20211110_CA12-00005064  Presmar.pdf", "C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas")

#"C:/Users/estev/Desktop/serviceContabilium/app_contabilium/api/api_contabilium/tests/facturas/000299_20211110_CA12-00005064  Presmar.pdf"



