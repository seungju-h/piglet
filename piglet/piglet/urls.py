"""
URL configuration for piglet project.

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('missinglist', views.missinglist, name='missinglist'),
    path('missinglistdetail', views.missinglistdetail, name='missinglistdetail'),
    path('reportmissing', views.reportmissing, name='reportmissing'),
    path('eventpage1', views.eventpage1, name='eventpage1'),
    path('eventpage2', views.eventpage2, name='run_model'),
    path('eventpage3', views.eventpage3, name='eventpage3'),
    path('process_upload', views.process_upload, name='process_upload'),
    path('dashboard', views.dashboard, name='dashboard'),
]
