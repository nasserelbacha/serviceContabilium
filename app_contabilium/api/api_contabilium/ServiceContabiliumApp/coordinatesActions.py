from rest_framework.response import Response
from . import models
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import json

def getCoordinates(self, request, **args):
    coordinates = list(models.Coordinates.objects.filter(provider=args['providerId']).values()) 
    if len(coordinates) > 0:
            datos = {'message': "Success", 'coordiantes': coordinates}
    else:
            datos = {'message': "bill not found..."}
    return JsonResponse(datos)

def createCoordinate(self, request, **args):
    jd = json.loads(request.body)
    provider = models.Providers.objects.get(id=jd['provider'])
    if  provider :
        models.Coordinates.objects.create(name=jd['name'],
                                    provider=provider,
                                    x1=jd['x1'],
                                    x2=jd['x2'],
                                    y1=jd['y1'],
                                    y2=jd['y2'])
        return Response(jd)
    else:
        return JsonResponse({"result": "error", "message" : "mala aplicacion"})

def getCoordinateById(self, request, id):
    coordinate = list(models.Coordinates.objects.filter(id=id).values())
    if len(coordinate) > 0:
        datos = {'message': "Success", 'coordinate': coordinate}
    else:
        datos = {'message': 'coordinate not found...'}
        return JsonResponse(datos)

def updateCoordinate(self, request, id):
    jd = json.loads(request.body)
    coordinate = models.Coordinates.objects.get(id=id)
    if len(coordinate) > 0:
        coordinate.x1 = jd['x1']
        coordinate.x2 = jd['x2']
        coordinate.y1 = jd['y1']
        coordinate.y2 = jd['y2']
        coordinate.save()
        datos = {'message': "Success", 'coordinate': coordinate}
    else:
        datos = {'message': 'coordinate not found...'}
        return JsonResponse(datos)
    