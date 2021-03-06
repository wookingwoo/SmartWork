"""my_site_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('MainPages.urls')), # 주소 뒤에 아무것도 없으면 MainPage.urls로 이동
	path('msgboards/', include('MessageBoards.urls')), # 주소 뒤에 msgboards/가 오면 msgboards.urls로 이동
    path('login/', include('login.urls')), # 주소 뒤에 아무것도 없으면 MainPage.urls로 이동
	path('markdownx/', include('markdownx.urls')), # markdownx 모듈 사용했음
	path('admin/', include('AdminPages.urls')),
    path('accounts/', include('allauth.urls')), #django-allauth 모듈 사용했음
	path('vacation/', include('vacation.urls')),





]