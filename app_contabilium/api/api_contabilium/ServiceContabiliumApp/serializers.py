from rest_framework import serializers
from . import models

from rest_framework.fields import CharField, EmailField, BooleanField, IntegerField, UUIDField

class TypeDocSerializer(serializers.ModelSerializer):
    name = CharField(required=True)
    class Meta:
        model = models.TypeDoc
        fields = ('name',)
        
class CompanySerializer(serializers.ModelSerializer):
    email = EmailField(required=True)
    password = CharField(required=True)
    name = CharField(required=True)
    cuilt = CharField(required=True)
    class Meta:
        model = models.Companies
        fields = ('email', 'password', "name", "cuilt")

class EmployeeSerializer(serializers.ModelSerializer):
    email = EmailField(required=True)
    name = CharField(required=True)
    lastNames = CharField(required=True)
    password = CharField(required=True)
    isAdmin = BooleanField(required=True)
    company = UUIDField(required=True)

    
    class Meta:
        model = models.Employees
        fields = ('name', 'lastNames','email', 'password', 'isAdmin', 'company')
    

# class AuthenticationSerializer(serializers.ModelSerializer):
#     email = EmailField()
#     password = CharField(required=True)
#     findEmail = models.Companies.objects.filter(email=email).values()
#     print(findEmail)
    
