from rest_framework.response import Response
from . import models
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import json
import pytesseract
import cv2
import os
import urllib.request
import base64
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from pdf2image import convert_from_path

def getCoordinates(self, request, **args):
    coordinates = list(models.Coordinates.objects.filter(provider=args['providerId']).values()) 
    if len(coordinates) > 0:
            datos = {'message': "Success", 'coordiantes': coordinates}
    else:
            datos = {'message': "bill not found..."}
    return JsonResponse(datos)

def createCoordinate(self, request, **args):
    jd = json.loads(request.body)
    print (jd)
    provider = models.Providers.objects.get(id=jd['provider'])
    if  provider :
        models.Coordinates.objects.create(name=jd['name'],
                                    provider=provider,
                                    x1=jd['x1'],
                                    x2=jd['x2'],
                                    y1=jd['y1'],
                                    y2=jd['y2'])
        readbase64(jd)
        return Response(jd)
    else:
        return JsonResponse({"result": "error", "message" : "mala aplicacion"})

def readbase64(jd):
    codigo_base64 = jd['Image64']
    imagen_bytes = base64.b64decode(codigo_base64)
    imagen_numpy = np.frombuffer(imagen_bytes, np.uint8)
    Image = cv2.imdecode(imagen_numpy, cv2.IMREAD_COLOR)
    ROI = Image[jd['y1']:jd['y2'],jd['x1']:jd['x2'] ]
    text = (pytesseract.image_to_string(ROI))
    print(text)
    
def getCoordinateById(self, request, id):
    coordinate = list(models.Coordinates.objects.filter(id=id).values())
    if len(coordinate) > 0:
        datos = {'message': "Success", 'coordinate': coordinate}
    else:
        datos = {'message': 'coordinate not found...'}
        return JsonResponse(datos)

def updateCoordinate(self, request, id):
    jd = json.loads(request.body)
    coordinate = models.Coordinates.objects.get(id=id)
    if len(coordinate) > 0:
        coordinate.x1 = jd['x1']
        coordinate.x2 = jd['x2']
        coordinate.y1 = jd['y1']
        coordinate.y2 = jd['y2']
        coordinate.save()
        datos = {'message': "Success", 'coordinate': coordinate}
    else:
        datos = {'message': 'coordinate not found...'}
        return JsonResponse(datos)
    
   

def readimage(image_path):
    codigo_base64 = ""
    imagen_bytes = base64.b64decode(codigo_base64)
    imagen_numpy = np.frombuffer(imagen_bytes, np.uint8)
    Image = cv2.imdecode(imagen_numpy, cv2.IMREAD_COLOR)
    Image = cv2.imread(image_path)
    y = 350
    ROI = Image[60:y, 80:1600]
    text = (pytesseract.image_to_string(ROI))
    contador = 0
    while contador == 0:
         word = "CUIT:"
         position = text.find(word)
         if position != -1:
            following_text = text[position + len(word): position + len(word) + 18]
            contador = contador + 1
         else:
            word = "C.U.I.T." 
            position = text.find(word)
            if position != -1:
                following_text = text[position + len(word): position + len(word) + 18]
                contador = contador + 1
            else:
                y = y + 10
                ROI = Image[60:y , 80:1600]
                text = (pytesseract.image_to_string(ROI))

    numeros = ""
    for caracter in following_text:
        if caracter.isdigit():
            numeros += caracter
    print(numeros)
    
    tr