from rest_framework.response import Response
from . import models
from .serializers import CompanySerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import jwt, datetime
import json
import smtplib, ssl
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from rest_framework.response import Response

def getCompanies(self, request, **id):
    if (id):
        companies = list(models.Companies.objects.filter(id=id['id']).values())
        if len(companies) > 0:
            company= companies[0]
            datos = {'message': "Success", 'company': company}
        else:
            datos = {'message': "company not found..."}
        return JsonResponse(datos)
    else:
        companies = list(models.Companies.objects.values())
        if len(companies) > 0:
            datos = {'message': "Success", 'companies': companies}
        else:
            datos = {'message': "docs not found..."}
        return JsonResponse(datos)

def createCompany(self, request):
    data = JSONParser().parse(request)
    serializer = CompanySerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        email = data['email']
        sendCreateCompanyEmail(email)
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def activateCompany(self, request):
# data = JSONParser().parse(request)
    company = models.Companies.objects.get(email=email)
    if not company:
        raise ValidationError("company not found", 404)
    company.enabled = True
    company.save()
    return JsonResponse({
        "message": "success"
    })

def authCompany(self, request):
    data = JSONParser().parse(request)
    email = data['email']
    findCompany = list(models.Companies.objects.filter(email=email).values())
    if not findCompany:
        raise ValidationError("bad credentials", 400)
    findCompany = findCompany[0]
    password = data['password']
    if password != findCompany['password']:
        raise ValidationError('incorrect password', 400)
    if not findCompany['enabled']:
        raise AuthenticationFailed('company not enabled', 401)
    payload = {
        'company': {
            'email': findCompany['email'],
            'name': findCompany['name'],
            'id': str(findCompany['id']),
            'cuilt': findCompany['cuilt'],
            'enabled': findCompany['enabled']
            },
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    role = findCompany['role']
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.set_cookie(key='role', value=role, httponly=True)
    response.data = {
        'jwt': token
    }
    return response

def sendCreateCompanyEmail(email):
    html = '''
    <html>
        <body>
            <h1>Daily S&P 500 prices report</h1>
            <p>Hello, welcome to your report!</p>
        </body>
    </html>
    '''
    email_from = 'digitalprocessfy@gmail.com'
    password = 'ajnzcdyktyefkyuo'
    email_to = email
    date_str = pd.Timestamp.today().strftime('%Y-%m-%d')
    email_message = MIMEMultipart()
    email_message['From'] = email_from
    email_message['To'] = email_to
    email_message['Subject'] = f'Report email - {date_str}'
    email_message.attach(MIMEText(html, "html"))
    email_message.attach(MIMEText(html, "html"))
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, html)