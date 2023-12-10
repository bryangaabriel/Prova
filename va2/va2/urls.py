"""
URL configuration for va2 project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('aluno.urls')),
    path('api/', include('turma.urls')),
    path('api/', include('detalheturma.urls')),
    path('api/', include('Professor.urls')),
    path('api/', include('detalhecurso.urls')),
    path('api/', include('curso.urls')),
    path('api/', include('disciplina.urls')),
     path('api/', include('detalhedisciplina.urls')),
]

