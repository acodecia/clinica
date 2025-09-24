# config/urls.py
from django.contrib import admin
from django.urls import path, include # Importe include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinica.urls')), # Inclui as URLs do app clinica
]