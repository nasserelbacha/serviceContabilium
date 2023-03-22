from rest_framework.response import Response
from . import models
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import json

def getInfo(self, request, **args):
    infos = list(models.BillInfo.objects.filter(bill=args['billId']).values()) 
    if len(coordinates) > 0:
            datos = {'message': "Success", 'coordiantes': coordinates}
    else:
            datos = {'message': "bill not found..."}
    return JsonResponse(datos)

def createInfo(self, request, **args):
    jd = json.loads(request.body)
    provider = models.Providers.objects.get(id=jd['provider'])
    coordinate = models.Coordinates.objects.get(id=jd['coordinate'])
    if  provider :
        models.BillInfo.objects.create(
                                    provider=provider,
                                    coordinate=coordinate,
                                    data=jd['data'])
        return Response(jd)
    else:
        return JsonResponse({"result": "error", "message" : "mala aplicacion"})

def updateInfo(self, request, id):
    jd = json.loads(request.body)
    info = models.BillInfo.objects.get(id=id)
    if len(info) > 0:
        info.data = jd['data']
        info.save()
        datos = {'message': "Success", 'info': info}
    else:
        datos = {'message': 'info not found...'}
        return JsonResponse(datos)
    