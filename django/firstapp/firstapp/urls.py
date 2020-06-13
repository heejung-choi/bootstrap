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
    path('articles/', include('articles.urls')),
    # include : 어떤 파일 import 할거야?     
    # view-source:127.0.0.1:8000/ articles/ -> 이후에 붙은 것으로 알겠다...
    # 기존에 view-source:127.0.0.1:8000/index였다면 지금은 view-source:127.0.0.1:8000/articles/index가 된다.
    #path('pages/', include('pages.urls')),
    path('pages/', include('pages.urls')),
]
