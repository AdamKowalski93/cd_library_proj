"""cd_library_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from cd_library import views
from rest_framework import routers
from cd_library.views.Types import TypesView
from cd_library.views.TypesApi import *
from cd_library.views.Cds import Cds
from cd_library.views.CdAPI import Cd

# router = routers.DefaultRouter()
# router.register('cd', viewset=views.CdDescriptionView)
# router.register('types', viewset=TypesView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('types/', TypesView.as_view()),
    path('type/', Type.as_view()),
    path('type/<int:type_id>/', Type.as_view()),
    path('cds/', Cds.as_view()),
    path('cd/<int:cd_id>/', Cd.as_view()),
    path('cd/', Cd.as_view())
]
