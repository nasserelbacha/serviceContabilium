from django.db import models

# Create your models here.

class Users(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=233)
    lastName = models.CharField(max_length=233)
    email = models.EmailField(max_length=233)
    password = models.CharField(max_length=233)
    profiel_photo = models.ImageField()

class Proveedor(models.Model):
    proovedorId = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=233)
    coordenadas_x = models.IntegerField(max_length=233)
    coordenadas_y = models.IntegerField(max_length=233)
    name = models.CharField(max_length=233)

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField()
    user_id = models.CharField(max_length=233)
    proveedor_id = models.CharField(max_length=233)