"""firstapp URL Configuration

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
from django.contrib import admin
from django.urls import path, include
# include 생성.
from articles import views
from pages import views

# from pages import views as pages_view 이렇게 바꿀 수 있지만, 좋은 방법은 아니다.

urlpatterns = [
    path('admin/', admin.site.urls),
    # 기존의 것 path만 남긴 후 제거
    path('article/', include('articles.urls')),
    # include : 어떤 파일 import 할거야? 
    
]
