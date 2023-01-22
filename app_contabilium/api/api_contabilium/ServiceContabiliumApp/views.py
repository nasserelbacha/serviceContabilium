from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import TypeDocSerializer, CompanySerializer, EmployeeSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError
import json
from . import models
import jwt, datetime

# Create your views here.

def checkIfUserIsAutheticated(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated!', 401)

class TypeDocView(views.APIView):    
    def get(self, request, **id):
        checkIfUserIsAutheticated(request)
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
        
    def post(self, request):
        try:
            checkIfUserIsAutheticated(request)
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
        checkIfUserIsAutheticated(request)
        try:
            employees = list(models.Employees.objects.filter(company=id['id']).values())
            if len(employees) > 0:
                data = {'message': 'Success', 'employees': employees}
            else: 
                data = {'message': 'dont employees'}
            return JsonResponse(data)
        except JSONDecodeError:
                return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
            
    def post(self, request, **id):
        try:
            jd = json.loads(request.body)
            company = models.Companies.objects.get(email = jd['company'])
            models.Employees.objects.create(name=jd['name']
                                            ,lastNames=jd['lastNames'],
                                            email=jd['email'],
                                            isAdmin=jd['isAdmin'],
                                            password=jd['password'],
                                            enabled=jd['enabled'],
                                            company=company
                                            )
            return Response(jd)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)

class EmployeeByIdView(views.APIView):
    def get(self, request, id):
        checkIfUserIsAutheticated(request)
        try:
            employee = list(models.Employees.objects.filter(id=id).values())
            if len(employee) > 0:
                datos = {'message': "Success", 'employee': employee}
            else:
                datos = {'message': "employee not found..."}
            return JsonResponse(datos)
        except JSONDecodeError:
                return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
 
class ProovidersView(views.APIView):
    def get(self, request, **id):
        checkIfUserIsAutheticated(request)
        try:    
            prooviders = list(models.Providers.objects.filter(company=id['id']).values())
            if len(prooviders) > 0:
                data = {'message': 'Success', 'prooviders': prooviders}
            else: 
                data = {'message': 'dont prooviders'}
            return JsonResponse(data)
        except JSONDecodeError:
                return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
    def post(self, request, **id):
        checkIfUserIsAutheticated(request)
        try:
            jd = json.loads(request.body)
            company = models.Companies.objects.get(id=jd['company'])
            models.Providers.objects.create(name=jd['name'],
                                            company=company)
            return Response(jd)
        except ValueError:
            return JsonResponse({"result": "error", "message":"Json decoding error"}, status=400)   
        
class ProovidersByIdView(views.APIView):
    def get(self, request, id):
        checkIfUserIsAutheticated(request)
        try:                
            provider = list(models.Providers.objects.filter(id=id).values())
            if len(provider) > 0:
                datos = {'message': "Success", 'provider': provider}
            else:
                datos = {'message': "provider not found..."}
            return JsonResponse(datos)
        except JSONDecodeError:
                return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
            
class BillView(views.APIView):
    def get(self, request, **args,):
        checkIfUserIsAutheticated(request)
        try:
            bill = list(models.Bill.objects.filter(provider=args['providerId']).values()) 
            if len(bill) > 0:
                    datos = {'message': "Success", 'bill': bill}
            else:
                    datos = {'message': "bill not found..."}
            return JsonResponse(datos)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
    def post(self, request, **id):
        checkIfUserIsAutheticated(request)
        try:
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
        except ValueError:
            return JsonResponse({"result": "error", "message":"Json decoding error"}, status=400)   

class BillByIdView(views.APIView):
    def get(self, request, id):
        checkIfUserIsAutheticated(request)
        try:
            bill = list(models.Bill.objects.filter(id=id).values())
            if len(bill) > 0:
                datos = {'message': "Success", 'bill': bill}
            else:
                datos = {'message': 'bill not found...'}
            return JsonResponse(datos)
        except JSONDecodeError(datos):
            return JsonResponse({"result": "error", "message": "Json decoding error"}, status=400)

class AuthCompany(views.APIView):
    def post(self, request, **args):
        try:
            data = JSONParser().parse(request)
            email = data['email']
            findCompany = list(models.Companies.objects.filter(email=email).values())
            if not findCompany:
                raise ValidationError("bad credentials", 400)
            findCompany = findCompany[0]
            password = data['password']
            if password != findCompany['password']:
                raise ValidationError('incorrect password', 400)
            if not findCompany['enabled']:
                raise AuthenticationFailed('company not enabled', 401)
            payload = {
                'company': {
                    'email': findCompany['email'],
                    'name': findCompany['name'],
                    'id': str(findCompany['id']),
                    'cuilt': findCompany['cuilt'],
                    'enabled': findCompany['enabled']
                    },
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256')
            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            
            response.data = {
                'jwt': token
            }
            return response
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
        
class AuthEmployee(views.APIView):
     def post(self, request, **args):
        try:
            data = JSONParser().parse(request)
            email = data['email']
            findEmployee = list(models.Employees.objects.filter(email=email).values())
            if not findEmployee:
                raise ValidationError("bad credentials", 400)
            findEmployee = findEmployee[0]
            print(findEmployee)
            password = data['password']
            if password != findEmployee['password']:
                raise ValidationError('incorrect password', 400)
            if not findEmployee['enabled']:
                raise AuthenticationFailed('employee not enabled', 401)
            payload = {
                'employee': {
                    'email': findEmployee['email'],
                    'name': findEmployee['name'],
                    'id': str(findEmployee['id']),
                    'lastName': findEmployee['lastNames'],
                    'enabled': findEmployee['enabled'],
                    'company': str(findEmployee['company_id'])
                    },
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256')
            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            
            response.data = {
                'jwt': token
            }
            return response
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)

class ActivateCompany(views.APIView):
    def patch(self, request, email):
        try:
            # data = JSONParser().parse(request)
            company = models.Companies.objects.get(email=email)
            if not company:
                raise ValidationError("company not found", 404)
            company.enabled = True
            company.save()
            return JsonResponse({
                "message": "success"
            })
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)   
        
        
class ActivateUser(views.APIView):
    def patch(self, request, email):
        try:
            checkIfUserIsAutheticated(request)
            employee = models.Employees.objects.get(email=email)
            if not employee:
                raise ValidationError("company not found", 404)
            employee.enabled = True
            employee.save()
            return JsonResponse({
                "message": "success"
            })
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)     
        
class LogoutView(views.APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    
