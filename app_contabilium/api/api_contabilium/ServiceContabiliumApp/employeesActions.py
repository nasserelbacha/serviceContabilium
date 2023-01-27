from rest_framework.response import Response
from . import models
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import jwt, datetime
import json
from rest_framework.response import Response

def getEmployees(self, request, **id):
    employees = list(models.Employees.objects.filter(company=id['id']).values())
    if len(employees) > 0:
        data = {'message': 'Success', 'employees': employees}
    else: 
        data = {'message': 'dont employees'}
    return JsonResponse(data)

def createEmployee(self, request, **id):
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

def getEmployeeById(self, request, id):
    employee = list(models.Employees.objects.filter(id=id).values())
    if len(employee) > 0:
        datos = {'message': "Success", 'employee': employee}
    else:
        datos = {'message': "employee not found..."}
    return JsonResponse(datos)

def activateEmployee(self, request, email):
    employee = models.Employees.objects.get(email=email)
    if not employee:
            raise ValidationError("company not found", 404)
    employee.enabled = True
    employee.save()
    return JsonResponse({
        "message": "success"
    })
    
def updateEmployeeRole(self, request, email):
    employee = models.Employees.objects.get(email=email)
    if not employee:
        raise ValidationError("company not found", 404)
    role = employee.role
    if role == 'ROLE_EMPLOYEE':
        role = 'ROLE_MANAGER'
    else:
        role = 'ROLE_EMPLOYEE'
    employee.role = role
    employee.save()
    return JsonResponse({
        "message": "success",
        "role": employee.role
    })

def authEmployee(self, request, **args):
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
        role = findEmployee['role']
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.set_cookie(key='role', value=role, httponly=True)
        response.data = {
            'jwt': token
        }
        return response