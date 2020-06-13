from django.urls import path
from . import views

app_name= 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    # '' 기본값으로 저장이 된다. 
]