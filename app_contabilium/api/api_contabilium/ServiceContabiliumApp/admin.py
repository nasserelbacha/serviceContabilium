from django.contrib import admin
from .models import Companies
from .models import Employees
from .models import Providers
from .models import Bill

# Register your models here.
admin.site.register(Companies)
admin.site.register(Employees)
admin.site.register(Providers)
admin.site.register(Bill)

