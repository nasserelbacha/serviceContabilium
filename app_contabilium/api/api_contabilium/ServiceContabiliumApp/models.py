from django.db import models
import uuid

#[TODO] change ids with uuid
# Create your models here.

class Companies(models.Model):
    # id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=233, default='hola@gmail.com')
    password = models.CharField(max_length=233, default='')
#    employees = models.ForeignKey(Employees, on_delete=models.CASCADE)

class Employees(models.Model):
    # id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=233, default='')
    lastNamess = models.CharField(max_length=233, default='')
    email = models.EmailField(max_length=233, default='hola@gmail.com')
    password = models.CharField(max_length=233, default='')
    isAdmin = models.BooleanField(default=False)
    company = models.OneToOneField(Companies, on_delete= models.CASCADE, default=1)

class Providers(models.Model):
    # id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=233, default='')
#    company= models.OneToOneField(Companies, on_delete=models.CASCADE)
#    provider_config = models.ForeignKey(Bill, on_delete= models.CASCADE)

class TypeDoc(models.Model):
    # id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True,)
    name = models.CharField(max_length=255, null=True)

class Bill(models.Model):
    # id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    typedoc = models.ForeignKey(TypeDoc, on_delete= models.CASCADE, default=1)
    name = models.CharField(max_length=233, default='')
    coordate_x = models.IntegerField(default=1)
    coordate_y = models.IntegerField(default=1)
    provider = models.ForeignKey(Providers, on_delete= models.CASCADE, default=1)
    company = models.ForeignKey(Companies, on_delete= models.CASCADE, default=1)
    info = models.CharField(max_length=233, default='')

    