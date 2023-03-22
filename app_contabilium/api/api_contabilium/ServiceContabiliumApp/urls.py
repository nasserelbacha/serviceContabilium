from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from .views import CompaniesView, EmployeesView, ProovidersView, ProovidersByIdView, EmployeeByIdView, BillView, BillByIdView, AuthCompany, LogoutView, AuthEmployee, ActivateCompany, ActivateUser, UpdateRoleToUser, CoordinatesById, CoordinatesViews, BillInfo, BillInfoById
from django.conf import settings
from django.urls import path, include 
from . import views


urlpatterns = [
    path('companies', CompaniesView.as_view(), name='companies_list'),
    path('companies/<str:id>', CompaniesView.as_view(), name='companies_process'),
    path('companies/<str:id>/employees', EmployeesView.as_view(), name='employees_list'),
    path('companies/employees/<str:id>', EmployeeByIdView.as_view(), name='employees_process'),
    path('companies/employees/', EmployeesView.as_view(), name='employees_process'),
    path('companies/providers/<str:id>', ProovidersByIdView.as_view(), name='prooviders_process'),
    path('companies/<str:id>/providers', ProovidersView.as_view(), name='prooviders_list'),
    path('companies/providers/', ProovidersView.as_view(), name='prooviders_process'),
    path('companies/providers/<str:providerId>/bill', BillView.as_view(), name="bill_list"),
    path('companies/providers/bill/', BillView.as_view(), name="bill_list"),
    path('companies/providers/bill/<str:id>', BillByIdView.as_view(), name="bill_process"),
    path('auth/company', AuthCompany.as_view(), name='login_company'),
    path('auth/employee', AuthEmployee.as_view(), name='login_employee'),
    path('logout', LogoutView.as_view(), name='logout' ),
    path("companies/activate/<str:email>", ActivateCompany.as_view(), name='activate_company'),
    path("employee/activate/<str:email>", ActivateUser.as_view(), name='activate_employee'),
    path("employee/change-role/<str:email>", UpdateRoleToUser.as_view(), name='role_employee'),
    path('companies/providers/bill/<str:id>/info', BillInfo.as_view(), name="bill_info"),
    path('companies/providers/bill/info/<str:id>', BillByIdView.as_view(), name="bill_process"),
    path('companies/providers/<str:id>/coordinates', CoordinatesViews.as_view(), name="coordinates_list"),
    path('companies/providers/coordinates/<str:id>', CoordinatesById.as_view(), name="coordinates_proccess"),
]
