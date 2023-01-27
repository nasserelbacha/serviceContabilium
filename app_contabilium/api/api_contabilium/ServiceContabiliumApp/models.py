from django.db import models
import uuid

#[TODO] change ids with uuid
# Create your models here.

class Companies(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=233, default='hola@gmail.com', unique=True)
    name = models.CharField(max_length=233, default='', unique=True)
    password = models.CharField(max_length=233, default='')
    cuilt = models.CharField(max_length=233, default='', unique=True)
    enabled = models.BooleanField(default=False)
    role = models.CharField(max_length=233, default="ROLE_MANAGER")

class Employees(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=233, default='')
    lastNames = models.CharField(max_length=233, default='')
    email = models.EmailField(max_length=233, default='hola@gmail.com', unique=True)
    password = models.CharField(max_length=233, default='')
    isAdmin = models.BooleanField(default=False)
    enabled = models.BooleanField(default=False)
    company = models.ForeignKey(Companies, on_delete= models.CASCADE)
    role = models.CharField(max_length=233, default="ROLE_EMPLOYEE")

class Providers(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True,)
    name = models.CharField(max_length=233, default='')
    company= models.ForeignKey(Companies, on_delete=models.CASCADE)
    cuilt = models.CharField(max_length=233, default='', unique=True)
    # provider_config = models.ForeignKey(Bill, on_delete= models.CASCADE)

class coordinateStart(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True,)
    provider = models.ForeignKey(Providers, on_delete= models.CASCADE)
    valueX = models.IntegerField(default=0)
    valueY = models.IntegerField(default=0)
    name = models.CharField(max_length=233, default='', unique=True)
    
class coordinateEnd(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True,)
    provider = models.ForeignKey(Providers, on_delete= models.CASCADE)
    valueX = models.IntegerField(default=0)
    valueY = models.IntegerField(default=0)
    name = models.CharField(max_length=233, default='', unique=True)

class TypeDoc(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True,)
    name = models.CharField(max_length=255, null=True, unique=True)

class Bill(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    typedoc = models.ForeignKey(TypeDoc, on_delete= models.CASCADE)
    name = models.CharField(max_length=233, default='')
    coordate_x = models.IntegerField(default=1)
    coordate_y = models.IntegerField(default=1)
    provider = models.ForeignKey(Providers, on_delete= models.CASCADE)
    info = models.CharField(max_length=233, default='')

    