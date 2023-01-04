from django.db import models

# Create your models here.

class Companies(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=233)
    password = models.CharField(max_length=233)
    # UserIds
    # ProovedorIds

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=233)
    lastName = models.CharField(max_length=233)
    email = models.EmailField(max_length=233)
    password = models.CharField(max_length=233)
    
class Providers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=233)
    #provider_config

class Coordenates(models.Model):
    id = models.AutoField(primary_key=True)
    name: models.CharField(max_length=233)
    coordate_x = models.IntegerField()
    coordate_y = models.IntegerField()
    provider_id = models.CharField(max_length=233)
    company_id = models.CharField(max_length=233)
    
class Bill (models.Model):
    id : models.AutoField(primary_key=True)
    bill_link = models.CharField(max_length=233)
    # bill_info 
    
    
