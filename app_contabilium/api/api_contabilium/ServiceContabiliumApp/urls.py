from django.urls import path, re_path
from . import views

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