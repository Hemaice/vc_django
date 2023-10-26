from django.urls import path
from . import views
urlpatterns=[
    path("vclogin/",views.vclogin,name='vclogin'),
    path("vcgetstart/",views.vcgetstart,name='vcgetstart'),
    path("vccourse/",views.vccourse,name='vccourse'),
    path("vcassignmet/",views.vcassignmet,name='vcassignmet'),
    path("vcasssubmitted/",views.vcasssubmitted,name='vcasssubmitted'),
    path("vcuploadfile/",views.vcuploadfile,name='vcuploadfile'),
    path("vchome/",views.vchome,name='vchome'),
]