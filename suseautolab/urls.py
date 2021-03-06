"""suseautolab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
#from django.contrib import admin

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#]
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.search_module),
    path('runoob/', views.runoob),
    url(r'^search-form/$', views.search_form),
    url(r'^search_result/$', views.search_result),
    url(r'^search_module/$', views.search_module),
    ]
