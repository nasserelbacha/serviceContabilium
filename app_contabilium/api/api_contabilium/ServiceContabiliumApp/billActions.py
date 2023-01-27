from rest_framework.response import Response
from . import models
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import json

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
    typeDoc = models.TypeDoc.objects.get(id=jd['typedoc'])
    if  provider and typeDoc:
        models.Bill.objects.create(name=jd['name'],
                                    typedoc=typeDoc,
                                    coordate_x=jd['coordatex'],
                                    coordate_y=jd['coordatey'],
                                    provider=provider,
                                    info=jd['info'])
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