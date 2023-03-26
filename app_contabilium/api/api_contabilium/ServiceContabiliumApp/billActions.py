from rest_framework.response import Response
from . import models
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import json
from pdf2image import convert_from_bytes
import io
import base64


def getBills(self, request, **args):
    bill = list(models.Bill.objects.filter(provider=args['providerId']).values()) 
    if len(bill) > 0:
            datos = {'message': "Success", 'bill': bill}
    else:
            datos = {'message': "bill not found..."}
    return JsonResponse(datos)

def createBill(self, request, **args):
    jd = json.loads(request.body)
    provider = models.Providers.objects.get(id=jd['provider'])
    if  provider:
        models.Bill.objects.create(name=jd['name'],
                                    provider=provider,
                                    )
        return Response(jd)
    else:
        return JsonResponse({"result": "error", "message" : "mala aplicacion"})
    
def getBillById(self, request, id):
    bill = list(models.Bill.objects.filter(id=id).values())
    if len(bill) > 0:
        datos = {'message': "Success", 'bill': bill}
    else:
        datos = {'message': 'bill not found...'}
        return JsonResponse(datos)

def pdf2Image(self, request, **args):
    file = request.FILES["fileName"]
    pages = convert_from_bytes(file.read(), 500, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    for page in pages:
        in_mem_file = io.BytesIO()
        page.save(in_mem_file , format = "png")
        in_mem_file.seek(0)
        imagebase64 = in_mem_file.getvalue()
        break
    encoded_string = base64.b64encode(in_mem_file.read())
    encoded_string = str(encoded_string)
    datos = {'message': "datos", "image": encoded_string}
    return JsonResponse(datos)

