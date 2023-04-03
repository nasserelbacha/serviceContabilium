from rest_framework.response import Response
from . import models
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import json

def getProviders(self, request, **id):
    prooviders = list(models.Providers.objects.filter(company=id['id']).values())
    if len(prooviders) > 0:
        data = {'message': 'Success', 'prooviders': prooviders}
    else: 
        data = {'message': 'dont prooviders'}
    return JsonResponse(data)

def createProvider(self, request,**id):
    jd = json.loads(request.body)
    company = models.Companies.objects.get(id=jd['company'])
    models.Providers.objects.create(name=jd['name'],
                                    company=company)
    return Response(jd)

def getProviderById(self, request, id):
    provider = list(models.Providers.objects.filter(id=id).values())
    if len(provider) > 0:
        datos = {'message': "Success", 'provider': provider}
    else:
        datos = {'message': "provider not found..."}
    return JsonResponse(datos)