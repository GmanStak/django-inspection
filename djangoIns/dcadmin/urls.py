from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('add/', views.add),
    path('hostAdd/', views.hostAdd),
    path('deviceadd/', views.addhostdevice),
    path('device/', views.device),
    path('insadd/', views.addInsGroup),
    path('insinfo/', views.insinfo),
    path('info/', views.info),
    path('insHost/', views.insHost),
    re_path(r"^(\d+)/delete", views.hostDel),
    re_path(r"^(\d+)/update", views.hostEdit),
]