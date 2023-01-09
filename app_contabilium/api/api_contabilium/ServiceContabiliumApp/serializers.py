from rest_framework import serializers
from . import models
from rest_framework.fields import CharField, EmailField, BooleanField, IntegerField, SlugField

class TypeDocSerializer(serializers.ModelSerializer):
    name = CharField(required=True)
    class Meta:
        model = models.TypeDoc
        fields = ('name',)
        
class CompanySerializer(serializers.ModelSerializer):
    email = EmailField(required=True)
    password = CharField(required=True)
    class Meta:
        model = models.Companies
        fields = ('email', 'password')

class EmployeeSerializer(serializers.ModelSerializer):
    email = EmailField(required=True)
    name = CharField(required=True)
    lastNamess = CharField(required=True)
    password = CharField(required=True)
    isAdmin = BooleanField(required=True)
    
    class Meta:
        model = models.Employees
        fields = ('name', 'lastNamess','email', 'password', 'isAdmin')
    
