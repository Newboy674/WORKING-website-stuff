"""Epicwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('tutorialstuff/', include('tutorialstuff.urls')),
    path('hello2/', include('hello2.urls')),
    path('secret/', include('secret.urls')),   ##FILE in the brackets matters, the XXXX/ is the name u type in 4 site
    path('hello/', include('hello.urls')),
    path('hello/', include('tutorialstuff.urls')),
    path('admin/',admin.site.urls),
]
