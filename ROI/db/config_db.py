import os
from dotenv import load_dotenv
import pyodbc


load_dotenv()

DATABASES = {
    'ENGINE': 'pyodbc',
    'DRIVER': os.getenv("DATABASE_DRIVER"),
    'HOST': os.getenv("DATABASE_HOST"),
    'USER': os.getenv("DATABASE_USER"),
    'PASSWORD': os.getenv("DATABASE_PWD"),
    'NAME': os.getenv("DATABASE_NAME"),
    'PORT': os.getenv('PORT')
}

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=" + DATABASES['HOST'] +"," + DATABASES['PORT'] +
            ";Database=" + DATABASES['NAME'] +
            ";UID=" + DATABASES['USER'] +";PWD=" + DATABASES['PASSWORD'])

cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()

print(cursor.execute("SELECT TOP(100) * FROM [users]"))

