"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', listen),
    path('food/', get_food),
    path('entertainment/', get_entertainment),
    path('cultural & historical/', get_cultural),
    path('outdoor activities/', get_outdoor),
    path('trips/', get_trips),
    path('get drunk/', get_drunk),
    path('student/', get_student),
    path('friends/', get_friends),
    path('family/', get_family),
    path('couples/', get_couples),
    path('tourists/', get_tourists),
]
