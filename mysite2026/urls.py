"""
URL configuration for mysite2026 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.http import HttpResponse


def info(request) :
    ip_address = request.META['REMOTE_ADDR']
    res_text = f"<h1> IP address ของเจ้าคือ {ip_address} </h1>"
    
    for k,v in request.META.items() :
        res_text += f"<p>{k} : {v} </p>"

    return HttpResponse(res_text) 


urlpatterns = [path('info/',info),
    path('admin/', admin.site.urls),
]
