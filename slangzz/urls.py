"""slangzz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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


from django.conf.urls import *

from django.contrib import admin
from myapp import views
from django.views.generic import TemplateView
#from myapp.views import GetSlangzz

'''
urlpatterns = [
    path('admin/', admin.site.urls),
 #   path('', GetSlangzz.as_view(template_name='index.html'), name='Index View'),
]



urlpatterns = [
    path('', views.index, name='index'),
]

'''
urlpatterns = [

  
    url('', views.index, name='index'),
    url(r'add/',views.add,name='add'),
]