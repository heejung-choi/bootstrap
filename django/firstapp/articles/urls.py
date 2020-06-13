from django.urls import path
from . import views 
# import view와 같지만 명시적으로 위와 같이 해주는 것을 좋아한다.

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('hello/<str:name>/', views.hello),
    # str 타입 명시는 생략 가능
    # path('hello/<name>/', views.hello),
    path('introduce/<name>/<int:age>/', views.introduce),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('dtl-practice/', views.dtl_practice),
    path('ispal/<word>/', views.ispal),
    path('throw/', views.throw),
    path('catch/',views.catch),
    path('req/',views.req),
    path('name/',views.name),
    path('artii/',views.artii, name='artii'),
    path('artii-result/',views.artii_result, name='artii_result') ,
]
