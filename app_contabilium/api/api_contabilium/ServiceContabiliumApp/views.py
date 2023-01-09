from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import TypeDocSerializer, CompanySerializer, EmployeeSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from . import models

# Create your views here.

class TypeDocView(views.APIView):    
    def get(self, request, **id):
        if (id):
            docs = list(models.TypeDoc.objects.filter(id=id['id']).values())
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
    def get(self, request, **id):
        if (id):
            companies = list(models.Companies.objects.filter(id=id['id']).values())
            if len(companies) > 0:
                company= companies[0]
                datos = {'message': "Success", 'company': company}
            else:
                datos = {'message': "company not found..."}
            return JsonResponse(datos)
        else:
            companies = list(models.Companies.objects.values())
            if len(companies) > 0:
                datos = {'message': "Success", 'companies': companies}
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
    def get(self, request, **id):
        try:
            employees = list(models.Employees.objects.filter(company=id).values())
            if len(employees) > 0:
                data = {'message': 'Success', 'employees': employees}
            else: 
                data = {'message': 'dont employees'}
            return JsonResponse(data)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            data['company'] = models.Companies.objects.get(id = data['company'])
            serializer = EmployeeSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)