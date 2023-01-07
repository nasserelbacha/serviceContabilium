#from django.urls import path, re_path
#from . import views
#from django.conf.urls.static import static
#from django.conf import settings

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