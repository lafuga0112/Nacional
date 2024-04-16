"""
URL configuration for HolaMundo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MundoOscuro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Loco, name='Loco'),
    path('Guardar/', guardar_perfil, name='guardar_perfil'),
    path('Guardar2/', guardar_perfil2, name='guardar_perfil2'),
    path('<str:cadena>/', Index, name='guardar_perfil_cadena'),  # Captura cualquier cadena de texto y la dirige a guardar_perfil
]
