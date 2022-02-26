"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import viewsMy Request
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
from rest_framework import urls
from cuser import views as regi_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', regi_view.RegisterView.as_view()),
    path('api/login/', regi_view.LoginView.as_view()),
    path('api/uniquecheck/', regi_view.EmailUniqueView.as_view()),
    path('api/todolist/', include('board.urls')),
]
