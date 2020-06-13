from django.urls import views

app_name= 'pages'

urlpatterns = [
    path('index/', views.index, name="index"),
]
