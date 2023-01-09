#from django.urls import path, re_path
#from . import views
#from django.conf.urls.static import static
#from django.conf import settings

<<<<<<< HEAD
from django.conf.urls.static import static
from .views import TypeDocView, CompaniesView, EmployeesView
from django.conf import settings

urlpatterns = [
    path('typesDoc/', TypeDocView.as_view(), name='type_doc_list'),
    path('typesDoc/<int:id>', TypeDocView.as_view(), name='type_doc_process'),
    path('companies/', CompaniesView.as_view(), name='companies_list'),
    path('companies/<int:id>', CompaniesView.as_view(), name='companies_process'),
    path('companies/employees', EmployeesView.as_view(), name='employees_list'),
]
=======
from django.urls import path
from .views import TypeDocView

urlpatterns = [
    path('typedocs/', TypeDocView.as_view(), name='TypeDoc_List')
]
#http://127.0.0.1:8000/ServiceContabiliumApp/typedocs/

#     re_path(r'^users/$',views.usersApi, name ='users'),
#     # path(r'^users/([0-9]+)$',views.usersApi),
    
#     path('proveedores',views.proveedorApi),
#     # path(r'^proveedores/([0-9]+)$',views.proveedorApi),
    
# 
>>>>>>> develop
