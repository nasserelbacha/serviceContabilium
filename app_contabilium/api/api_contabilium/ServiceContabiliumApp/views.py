<<<<<<< HEAD
from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import TypeDocSerializer, CompanySerializer, EmployeeSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from . import models
=======
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import TypeDoc

# from ServiceContabiliumApp.models import Users, Proveedor, Image
# from ServiceContabiliumApp.serializers import UsersSerializer,ProovedorSerializer, ImageSerializer

from django.core.files.storage import default_storage
from django.utils.decorators import method_decorator

class TypeDocView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request):
        Types= list(TypeDoc.objects.values())
        if len(Types)>0:
            datos = {'message':'Success', 'Types':Types}
        else:
            datos = {'message': 'Types not found'}
        return JsonResponse(datos)
        
    def post(self, request):
        datos = {'message':'Success'}
        return JsonResponse(datos)
>>>>>>> develop

# Create your views here.

class TypeDocView(views.APIView):    
    def get(self, request, id=0):
        if (id > 0):
            docs = list(models.TypeDoc.objects.filter(id=id).values())
            if len(docs) > 0:
                typeDoc = docs[0]
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
        
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = TypeDocSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)

class CompaniesView(views.APIView):
    def get(self, request, id=0):
        if (id > 0):
            companies = list(models.Companies.objects.filter(id=id).values())
            if len(companies) > 0:
                company= companies[0]
                datos = {'message': "Success", 'typeDoc': company}
            else:
                datos = {'message': "typeDoc not found..."}
            return JsonResponse(datos)
        else:
            companies = list(models.Companies.objects.values())
            if len(companies) > 0:
                datos = {'message': "Success", 'company': companies}
            else:
                datos = {'message': "docs not found..."}
            return JsonResponse(datos)
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = CompanySerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
        
class EmployeesView(views.APIView):
    def get(self, request, id):
        pass
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            data['company'] = models.Companies.objects.get(id = data['company'])
            print(data)
            serializer = EmployeeSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)