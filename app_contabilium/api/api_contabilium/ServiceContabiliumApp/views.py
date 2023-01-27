from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from json import JSONDecodeError
import jwt, datetime
from . import typeDocActions
from . import companiesActions
from . import employeesActions
from . import proovidersActions
from . import billActions

def checkIfUserIsAutheticated(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated!', 401)

def checkRoleManager(request):
    role = request.COOKIES.get('role')
    if role != "ROLE_MANAGER":
        raise ValidationError("permission denied", 401)    

def checkHasRole(request):
    role = request.COOKIES.get('role')
    if role!= "ROLE_EMPLOYEE" and role!="ROLE_MANAGER":
        raise ValidationError("permission denied", 401)

class TypeDocView(views.APIView):    
    def get(self, request, **id):
        checkIfUserIsAutheticated(request)
        checkHasRole(request)
        return typeDocActions.getTypeDoc(self, request, **id)
        
    def post(self, request):
        try:
            checkIfUserIsAutheticated(request)
            checkHasRole(request)
            return typeDocActions.postTypeDoc(self, request)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)

class CompaniesView(views.APIView):
    def get(self, request, **id):
        return companiesActions.getCompanies(self, request, **id)
    def post(self, request):
        try:
            return companiesActions.createCompany(self, request)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
        
class EmployeesView(views.APIView):
    def get(self, request, **id):
        checkIfUserIsAutheticated(request)
        checkRoleManager(request)
        try:
            return employeesActions.getEmployees(self, request, **id)
        except JSONDecodeError:
                return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
            
    def post(self, request, **id):
        try:
            return employeesActions.createEmployee(self, request, **id)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)

class EmployeeByIdView(views.APIView):
    def get(self, request, id):
        checkIfUserIsAutheticated(request)
        checkRoleManager(request)
        try:
           return employeesActions.getEmployeeById(self, request, id)
        except JSONDecodeError:
                return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
 
class ProovidersView(views.APIView):
    def get(self, request, **id):
        checkIfUserIsAutheticated(request)
        checkHasRole(request)
        try:    
            return proovidersActions.getProviders(self, request, **id)
        except JSONDecodeError:
                return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
    def post(self, request, **id):
        checkIfUserIsAutheticated(request)
        try:
            return proovidersActions.createProvider(self, request, **id)
        except ValueError:
            return JsonResponse({"result": "error", "message":"Json decoding error"}, status=400)   
        
class ProovidersByIdView(views.APIView):
    def get(self, request, id):
        checkIfUserIsAutheticated(request)
        checkHasRole(request)
        try:                
           return proovidersActions.getProviderById(self, request, id)
        except JSONDecodeError:
                return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
            
class BillView(views.APIView):
    def get(self, request, **args,):
        checkIfUserIsAutheticated(request)
        checkHasRole(request)
        try:
            return billActions.getBills(self, request, **args) 
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
    def post(self, request, **id):
        checkIfUserIsAutheticated(request)
        checkHasRole(request)
        try:
            return billActions.createBill(self, request, **id)
        except ValueError:
            return JsonResponse({"result": "error", "message":"Json decoding error"}, status=400)   

class BillByIdView(views.APIView):
    def get(self, request, id):
        checkIfUserIsAutheticated(request)
        checkHasRole(request)
        try:
            return billActions.getBillById(self, request, id)
        except JSONDecodeError(datos):
            return JsonResponse({"result": "error", "message": "Json decoding error"}, status=400)

class AuthCompany(views.APIView):
    def post(self, request, **args):
        try:
           return companiesActions.authCompany(self, request)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
        
class AuthEmployee(views.APIView):
     def post(self, request, **args):
        try:
            return employeesActions.authEmployee(self, request, **args)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)

class ActivateCompany(views.APIView):
    def patch(self, request, email):
        try:
           return companiesActions.activateCompany(self, request)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)   
        
        
class ActivateUser(views.APIView):
    def patch(self, request, email):
        try:
            checkIfUserIsAutheticated(request)
            checkRoleManager(request)
            return employeesActions.activateEmployee(self, request, email)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)     
        
class UpdateRoleToUser(views.APIView):
    def patch(self, request, email):
        try:
            checkIfUserIsAutheticated(request)
            checkRoleManager(request)
            return employeesActions.updateEmployeeRole(self, request, email)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)     
        
class LogoutView(views.APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.delete_cookie('role')
        response.data = {
            'message': 'success'
        }
        return response
    
