from django.urls import path

from core import views


app_name = "core"

urlpatterns = [
    path('', views.home, name='index'),
    
    path('test/', views.testing_channel, name='testing')

]