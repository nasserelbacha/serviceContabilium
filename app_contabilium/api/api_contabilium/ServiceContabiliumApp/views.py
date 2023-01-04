from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# from ServiceContabiliumApp.models import Users, Proveedor, Image
# from ServiceContabiliumApp.serializers import UsersSerializer,ProovedorSerializer, ImageSerializer

from django.core.files.storage import default_storage

# Create your views here.

# @csrf_exempt
# def usersApi(request,id=0):
#     if request.method=='GET':
#         users = Users.objects.all()
#         users_serializer=UsersSerializer(users,many=True)
#         return JsonResponse(users_serializer.data,safe=False)
#     elif request.method=='POST':
#         user_data=JSONParser().parse(request)
#         users_serializer =UsersSerializer(data=user_data)
#         if users_serializer.is_valid():
#             users_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
#     elif request.method=='PUT':
#         user_data=JSONParser().parse(request)
#         user=Users.objects.get(userId=user_data['userId'])
#         users_serializer=UsersSerializer(user,data=user_data)
#         if users_serializer.is_valid():
#             users_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         user=Users.objects.get(UserId=id)
#         department.delete()
#         return JsonResponse("Deleted Successfully",safe=False)

# @csrf_exempt
# def proveedorApi(request,id=0):
#     if request.method=='GET':
#         proveedor = Proveedor().objects.all()
#         proveedor_serializer=ProovedorSerializer(proveedores,many=True)
#         return JsonResponse(proveedor_serializer.data,safe=False)
#     elif request.method=='POST':
#         proveedor_data=JSONParser().parse(request)
#         proveedor_serializer=ProovedorSerializer(data=proveedor_data)
#         if proveedor_serializer.is_valid():
#             proveedor_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
#     elif request.method=='PUT':
#         proveedor_data=JSONParser().parse(request)
#         employee=Proveedor().objects.get(proveedorId=proveedor_data['proovedorId'])
#         proveedor_serializer=ProovedorSerializer(employee,data=proveedor_data)
#         if proveedor_serializer.is_valid():
#             proveedor_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         proveedor=Proveedor().objects.get(proveedorId=id)
#         proveedor.delete()
#         return JsonResponse("Deleted Successfully",safe=False)
    
# @csrf_exempt
# def imageApi(request,id=0):
#     if request.method=='GET':
#         image = Image()().objects.all()
#         image_serializer=ImageSerializer()(images,many=True)
#         return JsonResponse(image_serializer.data,safe=False)
#     elif request.method=='POST':
#         image_data=JSONParser().parse(request)
#         image_serializer=ImageSerializer()(data=image_data)
#         if image_serializer.is_valid():
#             image_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
#     elif request.method=='PUT':
#         image_data=JSONParser().parse(request)
#         employee=Image()().objects.get(imageId=image_data['id'])
#         image_serializer=ImageSerializer()(employee,data=image_data)
#         if image_serializer.is_valid():
#             image_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         image=Image().objects.get(imageId=id)
#         image.delete()
#         return JsonResponse("Deleted Successfully",safe=False)

# @csrf_exempt
# def SaveFile(request):
#     file=request.FILES['file']
#     file_name=default_storage.save(file.name,file)
#     return JsonResponse(file_name,safe=False)