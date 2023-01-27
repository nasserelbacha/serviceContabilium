from rest_framework.parsers import JSONParser
from .serializers import TypeDocSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from . import models

def getTypeDoc(self, request, **id):
    if (id):
            docs = list(models.TypeDoc.objects.filter(id=id['id']).values())
            if len(docs) > 0:
                typeDoc = docs
                datos = {'message': "Success", 'typeDoc': typeDoc}
            else:
                datos = {'message': "typeDoc not found..."}
            return JsonResponse(datos)
    else:
        docs = list(models.TypeDoc.objects.values())
        if len(docs) > 0:
            datos = {'message': "Success", 'docs': docs}
        else:
            datos = {'message': "docs not found..."}
        return JsonResponse(datos)

def postTypeDoc(self, request):
    data = JSONParser().parse(request)
    serializer = TypeDocSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)