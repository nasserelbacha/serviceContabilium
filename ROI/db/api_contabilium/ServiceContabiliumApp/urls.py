from django.urls import path, re_path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^users/$',views.usersApi, name ='users'),
    # path(r'^users/([0-9]+)$',views.usersApi),
    
    path('proveedores',views.proveedorApi),
    # path(r'^proveedores/([0-9]+)$',views.proveedorApi),
    
]