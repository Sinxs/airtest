"""Controller URL Configuration

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
from django.urls import path
from django.conf.urls import url
from Model import views, basehtml, case, login, report, index
from django.conf import settings
from django.views import static

#  被访问网址/ 模块.函数
urlpatterns = [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    path('admin/', admin.site.urls),
    path('platform/', views.platform),
    path('index/', index.start),
    path('login/', login.user_login, name='login'),
    path('report/', report.status),
    path('info/', report.reportinfo),
    path('base/', basehtml.base),
    path('case/', case.progress),
    path('send/', report.setprogress),
    path('send/', report.setprogress)
]