"""django_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import path, include, re_path
from short_url_app import views

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('login/', LoginView.as_view(template_name='accounts/login.html')),
    path('', lambda _ : redirect('./url/')),
    path('url/', views.UrlView.as_view()),
    path('show-url/', views.UrlView.as_view()),
    re_path(r'^(?P<short_url>[0-9a-zA-Z]{6})\/?$', views.GeneratedUrlView.as_view()),
    path('sign-up/', views.SignUp.as_view()),
    # path('url/', views.index)
]
